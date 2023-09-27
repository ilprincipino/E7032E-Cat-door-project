from machine import Pin, Timer
import time

led1 = Pin(18, Pin.OUT) 				  #Red
led2 = Pin(19, Pin.OUT)					  #Green
led3 = Pin(20, Pin.OUT) 				  #Blue
button2 = Pin(27, Pin.IN, Pin.PULL_DOWN)  #High button
button1 = Pin(21, Pin.IN, Pin.PULL_DOWN)  #Low button


#For-loop defines how many times the LED should blink
def blink(led):
    for i in range(3):
        led.toggle()
        time.sleep(0.3)
        led.toggle()
        time.sleep(0.3)
 
#Time sleep defines how long the LED is on
def static(led):
    led.on()
    time.sleep(1)
    led.off()

def pickButton(button, led_a, led_b):
    while button.value()== 0:
        pass
    t=time.ticks_ms()
    time.sleep_ms(1)
    while button.value()== 1:
        pass
    t=time.ticks_diff(time.ticks_ms(),t)
    if t<1500:
        blink(led_a)
    else:
        static(led_b)

while True:
    if button1.value() == 0 and button2.value() == 0:
        pass
    elif button1.value() == 1 and button2.value() == 0:
        pickButton(button1, led2, led1)
    elif button2.value() == 1 and button1.value() == 0:
        pickButton(button2, led3, led1)
    else:
        print("Don't wanna")