import machine, ubluetooth
from micropython import const
import time

# Constants for Bluetooth scanning
_IRQ_SCAN_RESULT = const(5)
_IRQ_SCAN_DONE = const(6)

# Function to turn LED on or off
def turn(val):
    led.value(val)

# Function to blink LED twice
def blink_led():
    for _ in range(2):
        turn(1)
        time.sleep(0.5)  # Duration LED is on
        turn(0)
        time.sleep(0.5)  # Duration LED is off

# Function to parse advertising data
def parse_advertising_data(adv_data):
    i = 0
    result = {"name": None, "uuids": [], "payload": None}
    while i + 1 < len(adv_data):
        length = adv_data[i]
        if length == 0 or length == 0xFF:
            break
        type = adv_data[i + 1]
        data = adv_data[i + 2:i + length + 1]

        if type == 0x09:  # Complete Local Name
            result["name"] = bytes(data).decode()
        elif type in [0x02, 0x03]:  # 16-bit UUIDs
            for j in range(0, len(data), 2):
                result["uuids"].append(data[j] + (data[j+1] << 8))
        elif type == 0xFF:  # Manufacturer Specific Data
            result["payload"] = data

        i += length + 1
    return result




# Function to check if the scanned device matches criteria
def check_device(adv_data, addr):
    parsed_data = parse_advertising_data(adv_data)
    target_uuid = 0x181A  # Target UUID to look for

    # Check for the target UUID and print payload if available
    if target_uuid in parsed_data["uuids"]:
        print("Target device found:", addr)
        payload=bytearray(parsed_data["payload"]).decode('utf-8')
        print("Payload= ",payload)
        blink_led()
        bt.gap_scan(None, 1280000, 11250, True)
        timer.init(period=10000, mode=machine.Timer.ONE_SHOT, callback=restart_scan)

# Bluetooth interrupt handler
def bt_irq(event, data):
    if event == _IRQ_SCAN_RESULT:
        addr_type, addr, adv_type, rssi, adv_data = data
        pop = ':'.join(['%02X' % i for i in addr])
        try:
            check_device(adv_data, pop)
        except Exception as e:
            print(e)

# Timer callback to restart scan
def restart_scan(timer):
    bt.gap_scan(0, 1280000, 11250, True)

# Setup the LED pin
led = machine.Pin(2, machine.Pin.OUT)

# Setup Bluetooth
bt = ubluetooth.BLE()
bt.active(True)
bt.irq(bt_irq)
bt.gap_scan(0, 1280000, 11250, True)

# Setup Timer
timer = machine.Timer(-1)

print("Scanning started.")
