import RPi.GPIO as GPIO
from time import *

GPIO.setwarnings(False)
TRIG=23
ECHO=24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG,GPIO.OUT)
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
            
        pulse_duration=pulse_start - pulse_end
        distance=pulse_duration*17150
        distance=round(distance,2)
        
        if (distance>2 and distance <400):
            print("Distance",distance -0.5,"cm")
        else:
            print("Distance",distance -0.5,"cm")
            print("Out of Range")
            
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
