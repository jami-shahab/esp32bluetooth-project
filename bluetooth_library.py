


def const(expr: _T, /) -> _T:
    """
   Used to declare that the expression is a constant so that the compile can
   optimise it.  The use of this function should be as follows::
   
    from micropython import const
   
    CONST_X = const(123)
    CONST_Y = const(2 * CONST_X + 1)
   
   Constants declared this way are still accessible as global variables from
   outside the module they are declared in.  On the other hand, if a constant
   begins with an underscore then it is hidden, it is not available as a global
   variable, and does not take up any memory during execution.
   
   This `const` function is recognised directly by the MicroPython parser and is
   provided as part of the :mod:`micropython` module mainly so that scripts can be
   written which run under both CPython and MicroPython, by following the above
   pattern.
   """
       @overload
    def value(self) -> int:
        """
      This method allows to set and get the value of the pin, depending on whether
      the argument ``x`` is supplied or not.
      
      If the argument is omitted then this method gets the digital logic level of
      the pin, returning 0 or 1 corresponding to low and high voltage signals
      respectively.  The behaviour of this method depends on the mode of the pin:
      
        - ``Pin.IN`` - The method returns the actual input value currently present
          on the pin.
        - ``Pin.OUT`` - The behaviour and return value of the method is undefined.
        - ``Pin.OPEN_DRAIN`` - If the pin is in state '0' then the behaviour and
          return value of the method is undefined.  Otherwise, if the pin is in
          state '1', the method returns the actual input value currently present
          on the pin.
      
      If the argument is supplied then this method sets the digital logic level of
      the pin.  The argument ``x`` can be anything that converts to a boolean.
      If it converts to ``True``, the pin is set to state '1', otherwise it is set
      to state '0'.  The behaviour of this method depends on the mode of the pin:
      
        - ``Pin.IN`` - The value is stored in the output buffer for the pin.  The
          pin state does not change, it remains in the high-impedance state.  The
          stored value will become active on the pin as soon as it is changed to
          ``Pin.OUT`` or ``Pin.OPEN_DRAIN`` mode.
        - ``Pin.OUT`` - The output buffer is set to the given value immediately.
        - ``Pin.OPEN_DRAIN`` - If the value is '0' the pin is set to a low voltage
          state.  Otherwise the pin is set to high-impedance state.
      
      When setting the value this method returns ``None``.
      """
        
    @overload
    def value(self, x: Any, /) -> None:
        """
      This method allows to set and get the value of the pin, depending on whether
      the argument ``x`` is supplied or not.
      
      If the argument is omitted then this method gets the digital logic level of
      the pin, returning 0 or 1 corresponding to low and high voltage signals
      respectively.  The behaviour of this method depends on the mode of the pin:
      
        - ``Pin.IN`` - The method returns the actual input value currently present
          on the pin.
        - ``Pin.OUT`` - The behaviour and return value of the method is undefined.
        - ``Pin.OPEN_DRAIN`` - If the pin is in state '0' then the behaviour and
          return value of the method is undefined.  Otherwise, if the pin is in
          state '1', the method returns the actual input value currently present
          on the pin.
      
      If the argument is supplied then this method sets the digital logic level of
      the pin.  The argument ``x`` can be anything that converts to a boolean.
      If it converts to ``True``, the pin is set to state '1', otherwise it is set
      to state '0'.  The behaviour of this method depends on the mode of the pin:
      
        - ``Pin.IN`` - The value is stored in the output buffer for the pin.  The
          pin state does not change, it remains in the high-impedance state.  The
          stored value will become active on the pin as soon as it is changed to
          ``Pin.OUT`` or ``Pin.OPEN_DRAIN`` mode.
        - ``Pin.OUT`` - The output buffer is set to the given value immediately.
        - ``Pin.OPEN_DRAIN`` - If the value is '0' the pin is set to a low voltage
          state.  Otherwise the pin is set to high-impedance state.
      
      When setting the value this method returns ``None``.
      """
    def sleep(seconds): # real signature unknown; restored from __doc__
    """
    sleep(seconds)
    
    Delay execution for a given number of seconds.  The argument may be
    a floating point number for subsecond precision.
    """
    pass
def gap_scan(
        self,
        duration_ms: int,
        interval_us: int = 1280000,
        window_us: int = 11250,
        active: bool = False,
        /,
    ) -> None:
        """
       Run a scan operation lasting for the specified duration (in **milli**\ seconds).
       
       To scan indefinitely, set *duration_ms* to ``0``.
       
       To stop scanning, set *duration_ms* to ``None``.
       
       Use *interval_us* and *window_us* to optionally configure the duty cycle.
       The scanner will run for *window_us* **micro**\ seconds every *interval_us*
       **micro**\ seconds for a total of *duration_ms* **milli**\ seconds. The default
       interval and window are 1.28 seconds and 11.25 milliseconds respectively
       (background scanning).
       
       For each scan result the ``_IRQ_SCAN_RESULT`` event will be raised, with event
       data ``(addr_type, addr, adv_type, rssi, adv_data)``.
       
       ``addr_type`` values indicate public or random addresses:
           * 0x00 - PUBLIC
           * 0x01 - RANDOM (either static, RPA, or NRPA, the type is encoded in the address itself)
       
       ``adv_type`` values correspond to the Bluetooth Specification:
       
           * 0x00 - ADV_IND - connectable and scannable undirected advertising
           * 0x01 - ADV_DIRECT_IND - connectable directed advertising
           * 0x02 - ADV_SCAN_IND - scannable undirected advertising
           * 0x03 - ADV_NONCONN_IND - non-connectable undirected advertising
           * 0x04 - SCAN_RSP - scan response
       
       ``active`` can be set ``True`` if you want to receive scan responses in the results.
       
       When scanning is stopped (either due to the duration finishing or when
       explicitly stopped), the ``_IRQ_SCAN_DONE`` event will be raised.
      """
        
   
class Timer:
    """
   Hardware timers deal with timing of periods and events. Timers are perhaps
   the most flexible and heterogeneous kind of hardware in MCUs and SoCs,
   differently greatly from a model to a model. MicroPython's Timer class
   defines a baseline operation of executing a callback with a given period
   (or once after some delay), and allow specific boards to define more
   non-standard behaviour (which thus won't be portable to other boards).
   
   See discussion of :ref:`important constraints <machine_callbacks>` on
   Timer callbacks.
   
   .. note::
   
       Memory can't be allocated inside irq handlers (an interrupt) and so
       exceptions raised within a handler don't give much information.  See
       :func:`micropython.alloc_emergency_exception_buf` for how to get around this
       limitation.
   
   If you are using a WiPy board please refer to :ref:`machine.TimerWiPy <machine.TimerWiPy>`
   instead of this class.
   """

    ONE_SHOT: ClassVar[int] = ...
    """
Timer operating mode.
   """

    PERIODIC: ClassVar[int] = ...
    """
Timer operating mode.
   """
        @overload
    def __init__(self, id: int, /):
        """
      Construct a new timer object of the given ``id``. ``id`` of -1 constructs a
      virtual timer (if supported by a board).
      ``id`` shall not be passed as a keyword argument.
      
      See ``init`` for parameters of initialisation.
      """
    @overload
    def __init__(self, id: int, /):
        """
      Construct a new timer object of the given ``id``. ``id`` of -1 constructs a
      virtual timer (if supported by a board).
      ``id`` shall not be passed as a keyword argument.
      
      See ``init`` for parameters of initialisation.
      """
 
    def init(
        self,
        *,
        mode: int = PERIODIC,
        period: int = -1,
        callback: Callable[[Timer], None] | None = None,
    ) -> None:
        """
      Initialise the timer. Example::
      
          def mycallback(t):
              pass
      
          # periodic with 100ms period
          tim.init(period=100, callback=mycallback)
      
          # one shot firing after 1000ms
          tim.init(mode=Timer.ONE_SHOT, period=1000, callback=mycallback)
      
      Keyword arguments:
      
        - ``mode`` can be one of:
      
          - ``Timer.ONE_SHOT`` - The timer runs once until the configured
            period of the channel expires.
          - ``Timer.PERIODIC`` - The timer runs periodically at the configured
            frequency of the channel.
 - ``period`` - The timer period, in milliseconds.
      
        - ``callback`` - The callable to call upon expiration of the timer period.
          The callback must take one argument, which is passed the Timer object.
          The ``callback`` argument shall be specified. Otherwise an exception
          will occurr upon timer expiration:
          ``TypeError: 'NoneType' object isn't callable``
      """
        
        
        
class Pin:
    """
   A pin object is used to control I/O pins (also known as GPIO - general-purpose
   input/output).  Pin objects are commonly associated with a physical pin that can
   drive an output voltage and read input voltages.  The pin class has methods to set the mode of
   the pin (IN, OUT, etc) and methods to get and set the digital logic level.
   For analog control of a pin, see the :class:`ADC` class.
   
   A pin object is constructed by using an identifier which unambiguously
   specifies a certain I/O pin.  The allowed forms of the identifier and the
   physical pin that the identifier maps to are port-specific.  Possibilities
   for the identifier are an integer, a string or a tuple with port and pin
   number.
   
   Usage Model::
   
       from machine import Pin
   
       # create an output pin on pin #0
       p0 = Pin(0, Pin.OUT)
   
       # set the value low then high
       p0.value(0)
       p0.value(1)
   
       # create an input pin on pin #2, with a pull up resistor
       p2 = Pin(2, Pin.IN, Pin.PULL_UP)
   
       # read and print the pin value
       print(p2.value())
   
       # reconfigure pin #0 in input mode with a pull down resistor
       p0.init(p0.IN, p0.PULL_DOWN)
   
       # configure an irq callback
       p0.irq(lambda p:print(p))
   """

    OUT: ClassVar[int] = ...
    """
Selects the pin mode.
   """
    
    class BLE:
    """
   class BLE
   ---------
   """
      @overload
    def active(self, active: bool, /) -> None:
        """
       Optionally changes the active state of the BLE radio, and returns the
       current state.
       
       The radio must be made active before using any other methods on this class.
      """
        def irq(self, handler: Callable[[int, tuple[memoryview, ...]], Any], /) -> None:
        """
       Registers a callback for events from the BLE stack. The *handler* takes two
       arguments, ``event`` (which will be one of the codes below) and ``data``
       (which is an event-specific tuple of values).
       
       **Note:** As an optimisation to prevent unnecessary allocations, the ``addr``,
       ``adv_data``, ``char_data``, ``notify_data``, and ``uuid`` entries in the
       tuples are read-only memoryview instances pointing to :mod:`bluetooth`'s internal
       ringbuffer, and are only valid during the invocation of the IRQ handler
       function.  If your program needs to save one of these values to access after
       the IRQ handler has returned (e.g. by saving it in a class instance or global
       variable), then it needs to take a copy of the data, either by using ``bytes()``
       or ``bluetooth.UUID()``, like this::
       
           connected_addr = bytes(addr)  # equivalently: adv_data, char_data, or notify_data
           matched_uuid = bluetooth.UUID(uuid)
       
       For example, the IRQ handler for a scan result might inspect the ``adv_data``
       to decide if it's the correct device, and only then copy the address data to be
       used elsewhere in the program.  And to print data from within the IRQ handler,
       ``print(bytes(addr))`` will be needed.
       
       An event handler showing all possible events::
       
           def bt_irq(event, data):
               if event == _IRQ_CENTRAL_CONNECT:
                   # A central has connected to this peripheral.
                   conn_handle, addr_type, addr = data
               elif event == _IRQ_CENTRAL_DISCONNECT:
                   # A central has disconnected from this peripheral.
                   conn_handle, addr_type, addr = data
               elif event == _IRQ_GATTS_WRITE:
                   # A client has written to this characteristic or descriptor.
                   conn_handle, attr_handle = data
               elif event == _IRQ_GATTS_READ_REQUEST:
                   # A client has issued a read. Note: this is only supported on STM32.
                   # Return a non-zero integer to deny the read (see below), or zero (or None)
                   # to accept the read.
                   conn_handle, attr_handle = data
               elif event == _IRQ_SCAN_RESULT:
                   # A single scan result.
                   addr_type, addr, adv_type, rssi, adv_data = data
               elif event == _IRQ_SCAN_DONE:
                   # Scan duration finished or manually stopped.
                   pass
               elif event == _IRQ_PERIPHERAL_CONNECT:
                   # A successful gap_connect().
                   conn_handle, addr_type, addr = data
               elif event == _IRQ_PERIPHERAL_DISCONNECT:
                   # Connected peripheral has disconnected.
                   conn_handle, addr_type, addr = data
               elif event == _IRQ_GATTC_SERVICE_RESULT:
                   # Called for each service found by gattc_discover_services().
                   conn_handle, start_handle, end_handle, uuid = data
               elif event == _IRQ_GATTC_SERVICE_DONE:
                   # Called once service discovery is complete.
                   # Note: Status will be zero on success, implementation-specific value otherwise.
                   conn_handle, status = data
               elif event == _IRQ_GATTC_CHARACTERISTIC_RESULT:
                   # Called for each characteristic found by gattc_discover_services().
                   conn_handle, def_handle, value_handle, properties, uuid = data
               elif event == _IRQ_GATTC_CHARACTERISTIC_DONE:
                   # Called once service discovery is complete.
                   # Note: Status will be zero on success, implementation-specific value otherwise.
                   conn_handle, status = data
               elif event == _IRQ_GATTC_DESCRIPTOR_RESULT:
                   # Called for each descriptor found by gattc_discover_descriptors().
                   conn_handle, dsc_handle, uuid = data
               elif event == _IRQ_GATTC_DESCRIPTOR_DONE:
                   # Called once service discovery is complete.
                   # Note: Status will be zero on success, implementation-specific value otherwise.
                   conn_handle, status = data
               elif event == _IRQ_GATTC_READ_RESULT:
                   # A gattc_read() has completed.
                   conn_handle, value_handle, char_data = data
               elif event == _IRQ_GATTC_READ_DONE:
                   # A gattc_read() has completed.
                   # Note: The value_handle will be zero on btstack (but present on NimBLE).
                   # Note: Status will be zero on success, implementation-specific value otherwise.
                   conn_handle, value_handle, status = data
               elif event == _IRQ_GATTC_WRITE_DONE:
                   # A gattc_write() has completed.
                   # Note: The value_handle will be zero on btstack (but present on NimBLE).
                   # Note: Status will be zero on success, implementation-specific value otherwise.
                   conn_handle, value_handle, status = data
               elif event == _IRQ_GATTC_NOTIFY:
                   # A server has sent a notify request.
                   conn_handle, value_handle, notify_data = data
               elif event == _IRQ_GATTC_INDICATE:
                   # A server has sent an indicate request.
                   conn_handle, value_handle, notify_data = data
               elif event == _IRQ_GATTS_INDICATE_DONE:
                   # A client has acknowledged the indication.
                   # Note: Status will be zero on successful acknowledgment, implementation-specific value otherwise.
                   conn_handle, value_handle, status = data
               elif event == _IRQ_MTU_EXCHANGED:
                   # ATT MTU exchange complete (either initiated by us or the remote device).
                   conn_handle, mtu = data
               elif event == _IRQ_L2CAP_ACCEPT:
                   # A new channel has been accepted.
                   # Return a non-zero integer to reject the connection, or zero (or None) to accept.
                   conn_handle, cid, psm, our_mtu, peer_mtu = data
               elif event == _IRQ_L2CAP_CONNECT:
                   # A new channel is now connected (either as a result of connecting or accepting).
                   conn_handle, cid, psm, our_mtu, peer_mtu = data
               elif event == _IRQ_L2CAP_DISCONNECT:
                   # Existing channel has disconnected (status is zero), or a connection attempt failed (non-zero status).
                   conn_handle, cid, psm, status = data
               elif event == _IRQ_L2CAP_RECV:
                   # New data is available on the channel. Use l2cap_recvinto to read.
                   conn_handle, cid = data
               elif event == _IRQ_L2CAP_SEND_READY:
                   # A previous l2cap_send that returned False has now completed and the channel is ready to send again.
                   # If status is non-zero, then the transmit buffer overflowed and the application should re-send the data.
                   conn_handle, cid, status = data
               elif event == _IRQ_CONNECTION_UPDATE:
                   # The remote device has updated connection parameters.
                   conn_handle, conn_interval, conn_latency, supervision_timeout, status = data
               elif event == _IRQ_ENCRYPTION_UPDATE:
                   # The encryption state has changed (likely as a result of pairing or bonding).
                   conn_handle, encrypted, authenticated, bonded, key_size = data
               elif event == _IRQ_GET_SECRET:
                   # Return a stored secret.
                   # If key is None, return the index'th value of this sec_type.
                   # Otherwise return the corresponding value for this sec_type and key.
                   sec_type, index, key = data
                   return value
               elif event == _IRQ_SET_SECRET:
                   # Save a secret to the store for this sec_type and key.
                   sec_type, key, value = data
                   return True
               elif event == _IRQ_PASSKEY_ACTION:
                   # Respond to a passkey request during pairing.
                   # See gap_passkey() for details.
                   # action will be an action that is compatible with the configured "io" config.
                   # passkey will be non-zero if action is "numeric comparison".
                   conn_handle, action, passkey = data
       
       
       The event codes are::
       
       from micropython import const
       _IRQ_CENTRAL_CONNECT = const(1)
       _IRQ_CENTRAL_DISCONNECT = const(2)
       _IRQ_GATTS_WRITE = const(3)
       _IRQ_GATTS_READ_REQUEST = const(4)
       _IRQ_SCAN_RESULT = const(5)
       _IRQ_SCAN_DONE = const(6)
       _IRQ_PERIPHERAL_CONNECT = const(7)
       _IRQ_PERIPHERAL_DISCONNECT = const(8)
       _IRQ_GATTC_SERVICE_RESULT = const(9)
       _IRQ_GATTC_SERVICE_DONE = const(10)
       _IRQ_GATTC_CHARACTERISTIC_RESULT = const(11)
       _IRQ_GATTC_CHARACTERISTIC_DONE = const(12)
       _IRQ_GATTC_DESCRIPTOR_RESULT = const(13)
       _IRQ_GATTC_DESCRIPTOR_DONE = const(14)
       _IRQ_GATTC_READ_RESULT = const(15)
       _IRQ_GATTC_READ_DONE = const(16)
       _IRQ_GATTC_WRITE_DONE = const(17)
       _IRQ_GATTC_NOTIFY = const(18)
       _IRQ_GATTC_INDICATE = const(19)
       _IRQ_GATTS_INDICATE_DONE = const(20)
       _IRQ_MTU_EXCHANGED = const(21)
       _IRQ_L2CAP_ACCEPT = const(22)
       _IRQ_L2CAP_CONNECT = const(23)
       _IRQ_L2CAP_DISCONNECT = const(24)
       _IRQ_L2CAP_RECV = const(25)
       _IRQ_L2CAP_SEND_READY = const(26)
       _IRQ_CONNECTION_UPDATE = const(27)
       _IRQ_ENCRYPTION_UPDATE = const(28)
       _IRQ_GET_SECRET = const(29)
       _IRQ_SET_SECRET = const(30)
       
       For the ``_IRQ_GATTS_READ_REQUEST`` event, the available return codes are::
       
       _GATTS_NO_ERROR = const(0x00)
       _GATTS_ERROR_READ_NOT_PERMITTED = const(0x02)
       _GATTS_ERROR_WRITE_NOT_PERMITTED = const(0x03)
       _GATTS_ERROR_INSUFFICIENT_AUTHENTICATION = const(0x05)
       _GATTS_ERROR_INSUFFICIENT_AUTHORIZATION = const(0x08)
       _GATTS_ERROR_INSUFFICIENT_ENCRYPTION = const(0x0f)
       
       For the ``_IRQ_PASSKEY_ACTION`` event, the available actions are::
       
       _PASSKEY_ACTION_NONE = const(0)
       _PASSKEY_ACTION_INPUT = const(2)
       _PASSKEY_ACTION_DISPLAY = const(3)
       _PASSKEY_ACTION_NUMERIC_COMPARISON = const(4)
       
       In order to save space in the firmware, these constants are not included on the
       :mod:`bluetooth` module. Add the ones that you need from the list above to your
       program.
      """
    def gap_scan(
        self,
        duration_ms: int,
        interval_us: int = 1280000,
        window_us: int = 11250,
        active: bool = False,
        /,
    ) -> None:
        """
       Run a scan operation lasting for the specified duration (in **milli**\ seconds).
       
       To scan indefinitely, set *duration_ms* to ``0``.
       
       To stop scanning, set *duration_ms* to ``None``.
       
       Use *interval_us* and *window_us* to optionally configure the duty cycle.
       The scanner will run for *window_us* **micro**\ seconds every *interval_us*
       **micro**\ seconds for a total of *duration_ms* **milli**\ seconds. The default
       interval and window are 1.28 seconds and 11.25 milliseconds respectively
       (background scanning).
       
       For each scan result the ``_IRQ_SCAN_RESULT`` event will be raised, with event
       data ``(addr_type, addr, adv_type, rssi, adv_data)``.
       
       ``addr_type`` values indicate public or random addresses:
           * 0x00 - PUBLIC
           * 0x01 - RANDOM (either static, RPA, or NRPA, the type is encoded in the address itself)
       
       ``adv_type`` values correspond to the Bluetooth Specification:
       
           * 0x00 - ADV_IND - connectable and scannable undirected advertising
           * 0x01 - ADV_DIRECT_IND - connectable directed advertising
           * 0x02 - ADV_SCAN_IND - scannable undirected advertising
           * 0x03 - ADV_NONCONN_IND - non-connectable undirected advertising
           * 0x04 - SCAN_RSP - scan response
       
       ``active`` can be set ``True`` if you want to receive scan responses in the results.
       
       When scanning is stopped (either due to the duration finishing or when
       explicitly stopped), the ``_IRQ_SCAN_DONE`` event will be raised.
      """
         def gap_advertise(
        self,
        interval_us: int,
        adv_data: AnyReadableBuf | None = None,
        /,
        *,
        resp_data: AnyReadableBuf | None = None,
        connectable: bool = True,
    ) -> None:
        """
       Starts advertising at the specified interval (in **micro**\ seconds). This
       interval will be rounded down to the nearest 625us. To stop advertising, set
       *interval_us* to ``None``.
       
       *adv_data* and *resp_data* can be any type that implements the buffer
       protocol (e.g. ``bytes``, ``bytearray``, ``str``). *adv_data* is included
       in all broadcasts, and *resp_data* is send in reply to an active scan.
       
       **Note:** if *adv_data* (or *resp_data*) is ``None``, then the data passed
       to the previous call to ``gap_advertise`` will be re-used. This allows a
       broadcaster to resume advertising with just ``gap_advertise(interval_us)``.
       To clear the advertising payload pass an empty ``bytes``, i.e. ``b''``.
      """
        
        
class Struct(object):
    """
    Create a compiled struct object.
    
    Return a new Struct object which writes and reads binary data according to
    the format string.
    
    See help(struct) for more on format strings.
    """
        def pack(self, *args): # known case of _struct.Struct.pack
        """
        S.pack(v1, v2, ...) -> bytes
        
        Return a bytes object containing values v1, v2, ... packed according
        to the format string S.format.  See help(struct) for more on format
        strings.
        """
        return b""