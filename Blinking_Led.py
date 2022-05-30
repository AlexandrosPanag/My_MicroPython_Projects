# This code was edited by Alexandros Panagiotakopoulos

from machine import Pin #importing the necessary libraries
import time

# Pin D9 (ON/SLEEP/DIO9)
LED_PIN_ID = "D9"


# Set up the LED pin object to manage the LED status. Configure the pin
# as output and set its initial value to off (0).
led_pin = Pin(LED_PIN_ID, Pin.OUT, value=0)

# Start blinking the LED by toggling its value every second.
while True: # begin eternal loop this code runs forever
    print("- LED OFF")
    led_pin.value(0) # turn off the LED
    time.sleep(1)  # delay 1 second

    print("- LED ON") # print LED on
    led_pin.value(1) # turn on the LED
    time.sleep(1) # delay 1 second
