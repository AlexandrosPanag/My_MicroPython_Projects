# code written by Alexandros Panagiotakopoulos

from machine import Pin
import time

# Pin D9 (ON/SLEEP/DIO9)
LED_PIN_ID = "D9"
cnt=0
i=0

# Set up the LED pin object to manage the LED status. Configure the pin
# as output and set its initial value to off (0).
led_pin = Pin(LED_PIN_ID, Pin.OUT, value=0)

# Start blinking the LED by toggling its value every second.
while True:
    print("\nGive the number of times for the device to blink:\n")
    x = int(input())
    print("\nThe device will blink", x,"times")
    for i in range(0,x):
        print("- LED OFF")
        led_pin.value(0)
        time.sleep(1)

        print("- LED ON")
        led_pin.value(1)
        time.sleep(1)
        cnt+=1
        print("\nThe LED has blinked", cnt, " times\n")

