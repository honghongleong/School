import RPi.GPIO as GPIO
from time import *

GPIO.setwarnings(False)
TRIG=23
ECHO=24
Red=13
Green=14
Yellow=15

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(Red,GPIO.OUT)
GPIO.setup(Green,GPIO.OUT)
GPIO.setup(Yellow,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

try:
    while True:
        GPIO.output(TRIG,False)
        print("waiting for sensor to settle")
        sleep(2)
        
        GPIO.output(TRIG,True)
        sleep(1)
        GPIO.output(TRIG,False)
        
        while GPIO.input(ECHO)==0:
            pulse_start = time()
            
        while GPIO.input(ECHO)==1:
            pulse_end = time()
            
        pulse_duration = pulse_end - pulse_start
        
        distance = pulse_duration*17150
        distance = round(distance,2)
        
        if (distance>0 and distance<20):
            print("Distance",distance -0.5,"cm")
            exec(open('./Stream.py').read()
            GPIO.output(Red, GPIO.HIGH)#Turn Red LED on
            GPIO.output(Green, GPIO.HIGH)#Turn Green LED on
            GPIO.output(Yellow, GPIO.HIGH)#Turn Yellow LED on
            sleep(0.5)# Delay for 0.5 second
            GPIO.output(Red, GPIO.LOW)#Turn LED off
            GPIO.output(Green, GPIO.LOW)#Turn LED off
            GPIO.output(Yellow, GPIO.LOW)#Turn LED off
            sleep(0.5)# Delay for 0.5 second
        elif (distance > 20 and distance < 30):
            print("Distance",distance -0.5,"cm")
            exec(open('./Stream.py').read()
            for x in range (0,2):
                GPIO.output(Red, GPIO.HIGH)#Turn Red LED on
                GPIO.output(Green, GPIO.HIGH)#Turn Green LED on
                GPIO.output(Yellow, GPIO.HIGH)#Turn Yellow LED on
                sleep(0.5)# Delay for 0.5 second
                GPIO.output(Red, GPIO.LOW)#Turn LED off
                GPIO.output(Green, GPIO.LOW)#Turn LED off
                GPIO.output(Yellow, GPIO.LOW)#Turn LED off
                sleep(0.5)# Delay for 0.5 second
                x=x+1
        else:
            print("Distance",distance -0.5,"cm")
            exec(open('./Stream.py').read()
            for x in range (0,3):
                GPIO.output(Red, GPIO.HIGH)#Turn Red LED on
                GPIO.output(Green, GPIO.HIGH)#Turn Green LED on
                GPIO.output(Yellow, GPIO.HIGH)#Turn Yellow LED on
                sleep(0.5)# Delay for 0.5 second
                GPIO.output(Red, GPIO.LOW)#Turn LED off
                GPIO.output(Green, GPIO.LOW)#Turn LED off
                GPIO.output(Yellow, GPIO.LOW)#Turn LED off
                sleep(0.5)# Delay for 0.5 second
                x=x+1
            
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()