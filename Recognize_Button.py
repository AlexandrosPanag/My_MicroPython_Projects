from machine import Pin
import xbee
import time

# Pin D0 (AD0/DIO0)
INPUT_PIN_ID = "D0"

# Pin D9 (ON/SLEEP/DIO9)
LED_PIN_ID = "D9"

# Set up the pin object to check the input value of the user button. Configure
# the pin as input and enable the internal pull-up.
input_pin = Pin(INPUT_PIN_ID, Pin.IN, Pin.PULL_UP)

# Set up the LED pin object to manage the LED status. Configure the pin
# as output and set its initial value to off (0).
led_pin = Pin(LED_PIN_ID, Pin.OUT, value=0)

xb = xbee.XBee()



while True:
    # Check if the switch is pressed.
    if input_pin.value() == 0:
        led_pin.value(1)  # turn on the LED
        time.sleep(1)  # delay 1 second
    else:
        led_pin.value(0)  # turn off the LED
        time.sleep(1)  # delay 1 second