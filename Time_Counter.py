# Time counter program
#
# Created by Alexandros Panagiotakopoulos
#

from machine import Pin
import time

# Pin D9 (ON/SLEEP/DIO9)
LED_PIN_ID = "D9"


timecount = 0

# Set up the LED pin object to manage the LED status. Configure the pin
# as output and set its initial value to off (0).
led_pin = Pin(LED_PIN_ID, Pin.OUT, value=0)

# Start blinking the LED by toggling its value every second.
while True:
    timecount+=1
    print("Counter is equal to: ",timecount)
    time.sleep(1)
