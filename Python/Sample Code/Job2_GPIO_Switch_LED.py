import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)


led_pin = 24        #Initializing pin 24 for led
button_pin=25       #Initializing pin 25 for button

GPIO.setmode(GPIO.BCM)	#Using BCM numbering

GPIO.setup(led_pin, GPIO.OUT) 	#Declare the led pin as output pin
GPIO.setup(button_pin, GPIO.IN) #Declare the button pin as input pin

try:
	while True:
	
		button_status = GPIO.input(button_pin)	#Read the button status

		if(button_status ==1):
			GPIO.output(led_pin, True)			#Turn on LED
			
		else:
			GPIO.output(led_pin, False)			#Turn off LED

except KeyboardInterrupt:	#if keyboard Interrupt (CTRL-C) is pressed
	pass					#Go to next line
	
finally:
	GPIO.cleanup()			#Make all GPIO pins low
