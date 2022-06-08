# User Input Blink
#
# Created by Alexandros Panagiotakopoulos
#

from machine import Pin
import time

# Pin D9 (ON/SLEEP/DIO9)
LED_PIN_ID = "D9"


led_pin = Pin(LED_PIN_ID, Pin.OUT, value=0)

# Force the user to enter in one of the two states
while True:
    x = input("Give one of the following numbers 1 to turn on the led or 0 to turn off the led:")
    if x == "1":
        print("- LED OFF")
        led_pin.value(0)
        time.sleep(10)
    elif x == "0":
        print("- LED ON")
        led_pin.value(1)
        time.sleep(10)
