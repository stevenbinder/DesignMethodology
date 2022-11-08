from RPi import GPIO
import time
import math
import numpy as np

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)

GPIO.setwarnings(False)

freq=0.001
T=1/freq

GPIO.output(37,GPIO.LOW)
GPIO.output(13,GPIO.LOW)
GPIO.output(31,GPIO.LOW)
GPIO.output(29,GPIO.LOW)

while True:

    sine=round((1+math.sin(2*math.pi*freq*(time.time())*100))*7.5,0)
    x=format(int(sine),'b')
    sinOut=x.rjust(4,'0')
    if sinOut[0]=='1':
        GPIO.output(37,GPIO.HIGH)
    elif sinOut[0]=='0':
        GPIO.output(37,GPIO.LOW)
    if sinOut[1]=='1':
        GPIO.output(13,GPIO.HIGH)
    elif sinOut[1]=='0':
        GPIO.output(13,GPIO.LOW)
    if sinOut[2]=='1':
        GPIO.output(31,GPIO.HIGH)
    elif sinOut[2]=='0':
        GPIO.output(31,GPIO.LOW)
    if sinOut[3]=='1':
        GPIO.output(29,GPIO.HIGH)
    elif sinOut[3]=='0':
        GPIO.output(29,GPIO.LOW)



GPIO.cleanup()

# b1=GPIO.PWM(37,(2*freq))
# b2=GPIO.PWM(13,(4*freq))
# b3=GPIO.PWM(31,(8*freq))
# b4=GPIO.PWM(29,(16*freq))
# 
# GPIO.output(37,GPIO.LOW)
# GPIO.output(13,GPIO.LOW)
# GPIO.output(31,GPIO.LOW)
# GPIO.output(29,GPIO.LOW)
# 
# b4.start(50)
# b3.start(50)
# b2.start(50)
# b1.start(50)
# 
# while True:
#     sleep(T/2)
#     b1.ChangeFrequency(16*freq)
#     b2.ChangeFrequency(8*freq)
#     b3.ChangeFrequency(4*freq)
#     b4.ChangeFrequency(2*freq)
# 
#     
# GPIO.cleanup()

