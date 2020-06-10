#Controlling a DC motor
#dcmotor.py

import RPi.GPIO as GPIO		
import time					

GPIO.setwarnings(False)

#Pins for motor driver inputs
Motor1A = 24					
Motor2A = 23
MotorEn = 25

def setup():
GPIO.setmode(GPIO.BCM)			
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(MotorEn, GPIO.OUT)

def loop():
	#going forwards
	GPIO.output(Motor1A, GPIO.HIGH)
	GPIO.output(Motor2A, GPIO.LOW)
	GPIO.output(MotorEn, GPIO.HIGH)
	
	time.sleep(5)
	#stop motor
	GPIO.output(MotorEn, GPIO.LOW)
	
def destroy():
	GPIO.cleanup()
	
#program start here
setup()

try:
	loop()
	
except KeyboardInterrupt:
	destroy()