from machine import Pin, Timer
import time

led = Pin(19, Pin.OUT)
button = Pin(21, Pin.IN, Pin.PULL_DOWN)
    
while True:
    if button.value():
        for i in range(5):		#Define how long the led should blink for
            led.toggle()
            time.sleep(0.5)
            led.toggle()
            time.sleep(0.5)
