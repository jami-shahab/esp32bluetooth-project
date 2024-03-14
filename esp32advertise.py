import machine, utime, ubluetooth
from ble_advertising import advertising_payload as adpl

# Initalize bluetooth and make it run!
pl = adpl(name='bluetooththingy', customData="red", services=[ubluetooth.UUID(0x181A)])
led = machine.Pin(2, machine.Pin.OUT)
bt = ubluetooth.BLE()
bt.active(True)
print('Bluetooth enabled.')

# Enable flag.
advertising = True
try:
    bt.gap_advertise(0, adv_data=pl, connectable=True)
except Exception as e:
    print("Error advertising:", e)
    advertising = False # Currently, this is the only time when the LED will shut off.
    
# Busy loop to keep everything running (and check LED status)!
while True:
    if advertising:
        # Turn LED on
        led.value(1)
    else:
        led.value(0)
    utime.sleep(10)
