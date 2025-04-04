from machine import Pin
from Servo import Servo
import time
leftMotor=Servo(pin=7)
rightMotor=Servo(pin=8)
#Left IR sensor
Left_Eye = Pin(16, Pin.IN)
#Right IR sensor
Right_Eye = Pin(17, Pin.IN)

def LeftMotorSpeed(speed):
    leftMotor.write(((speed+100)*180/200))
def RightMotorSpeed(speed):
    rightMotor.write(((speed+100)*180/200))
def stop():
    LeftMotorSpeed(0)
    RightMotorSpeed(0)
    time.sleep(0.2)
def forward(repeat, speedlevel):
    RightMotorSpeed(-1*speedlevel)
    LeftMotorSpeed(speedlevel)
    time.sleep(1*repeat)
def backward(repeat, speedlevel):
    RightMotorSpeed(speedlevel)
    LeftMotorSpeed(-1*speedlevel)
    time.sleep(1*repeat)
def left(repeat, speedlevel):
    RightMotorSpeed(-1*speedlevel-5)
    LeftMotorSpeed(-1*speedlevel-5)
    time.sleep(1*repeat)
def right(repeat, speedlevel):
    RightMotorSpeed(speedlevel)
    LeftMotorSpeed(speedlevel)
    time.sleep(1*repeat)
def run():
    try:
        time.sleep(0.2)
        while True:
            L=Left_Eye.value()
            R=Right_Eye.value()
            if L==0 and R==0:
                #Note: These speed values CAN be changed though it works properly as it without changing them with the correct design
                forward(0.001, 15)
            if L==1 and R==1:
                stop()
            if L==1 and R==0:
                left(0.001, 15)
            if L==0 and R==1:
                right(0.001, 15)
    except KeyboardInterrupt:
        stop()
if __name__=="__main__":
    run()
