from machine import Pin, Timer
import time

motor1 = Pin(19, Pin.OUT)
motor2 = Pin(20, Pin.OUT)
button2 = Pin(27, Pin.IN, Pin.PULL_DOWN)  #High button
button1 = Pin(21, Pin.IN, Pin.PULL_DOWN)  #Low button


def turnOn(motor_a, motor_b):
    motor_a.on()
    time.sleep(3)
    turnOff(motor_a)
    time.sleep(1)
    motor_b.on()
    time.sleep(3)
    turnOff(motor_b)
    
    
def turnOff(motor):
    motor.off()
    
#Using buttons for now, will get input from antenna later
while True:
    if button1.value() == 0 and button2.value() == 0:
        pass
    elif button1.value() == 1 and button2.value() == 0:
        turnOn(motor1, motor2)
    elif button2.value() == 1 and button1.value() == 0:
        turnOn(motor2, motor1)
    else:
        print("Don't wanna")