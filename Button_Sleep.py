# based on the PyCharm digixbee zigbee 3 meshkit example
# code written by Alexandros Panagiotakopoulos
from machine import Pin
import xbee


# Pin D0 (AD0/DIO0)
INPUT_PIN_ID = "D0"



# Set up the pin object to check the input value of the user button. Configure
# the pin as input and enable the internal pull-up.
input_pin = Pin(INPUT_PIN_ID, Pin.IN, Pin.PULL_UP)

xb = xbee.XBee()


while True:
    # Check if the switch is pressed.
    print("Press the button in order to sleep")
    if input_pin.value() == 0:
        # Sleep for 30 seconds and enable the early wake up with DTR pin.
        print("  - Sleeping for 10 seconds...")
        sleep_ms = xb.sleep_now(10000, True)
        # Module woke up.
        print("  - Woke up! Slept for %u ms" % sleep_ms)
        if xb.wake_reason() is xbee.PIN_WAKE:
            print("      * Woke early on DTR toggle")

        print("\nWaiting for 'User button' to be pressed to Sleep...")
