#Control a Servo Control

import RPi.GPIO as GPIO	#Import the GPIO library to use the GPIO pins of Raspberry Pi
import time				#Import the time library to provide the delays in the program

GPIO.setwarnings(False)

servo_pin = 18			#Initializing pin 18 for servo motor

GPIO.setmode(GPIO.BCM)			#Using BCM numbering
GPIO.setup(servo_pin, GPIO.OUT) #Declare the servo pin as output pin

pwm = GPIO.PWM(servo_pin, 50)	#Create PWM channel at 50Hz frequency
pwm.start(3)					#Start PWM at 0% duty cycle

try:
	while True:					#Loop will run forever
		pwm.ChangeDutyCycle(3)	#Move servo to 0 degrees
		time.sleep(1)			#Delay of 1 sec 
		
		pwm.ChangeDutyCycle(7)	#Move servo to 90 degrees
		time.sleep(1)			#Delay of 1 sec 
		
		pwm.ChangeDutyCycle(11.5)	#Move servo to 180 degrees
		time.sleep(1)			#Delay of 1 sec 

except KeyboardInterrupt:		#if keyboard Interrupt (CTRL-C) is pressed
	pass						#Go to next line
	
	pwm.stop()					#Stop the PWM
	
finally:
	GPIO.cleanup()				#Make all GPIO pins low