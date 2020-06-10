#LED Fading Up and Down using PWM.

import RPi.GPIO as GPIO	#Import the GPIO library to use the GPIO pins of Raspberry Pi
import time				#Import the time library to provide the delays in the program

GPIO.setwarnings(False)

led_pin = 24	#Initializing pin 24 for led
freq = 50		#Initializing freq to 50Hz

GPIO.setmode(GPIO.BCM)			#Using BCM numbering
GPIO.setup(led_pin, GPIO.OUT) 	#Declare the led pin as output pin

pwm = GPIO.PWM(led_pin, freq)	#Create a PWM object
pwm.start(0)					#Start PWM at 0% duty cycle

try:
	while True:
	# Fade Up
	for dc in range (0,100,5):	#Loop will run from 0 to 100, interval of 5
		pwm.ChangeDutyCycle(dc)
		time.sleep(0.1)

	# Fade Down
	for dc in range (100,0,-5):	#Loop will run from 100 to 0, interval of -5
		pwm.ChangeDutyCycle(dc)
		time.sleep(0.1)

except KeyboardInterrupt:		#if keyboard Interrupt (CTRL-C) is pressed
	pass						#Go to next line
	
	pwm.stop()					#Stop the PWM
	
finally:
	GPIO.cleanup()				#Make all GPIO pins low