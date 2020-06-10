import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

led_pin = 24	#Initializing pin 24 for LED

GPIO.setmode(GPIO.BCM)	#Using BCM numbering

GPIO.setup(led_pin,GPIO.OUT)	#Declare the led pin as output pin

try:
	#Loop for 5 times or until the user presses Ctrl+C
	for i in range(0,5):
		
		GPIO.output(led_pin, True) #Turn on LED for 1 second
		time.sleep(1)

		GPIO.output(led_pin,False) #Turn off LED for 1 second
		time.sleep(1)

except KeyboardInterrupt:	#if keyboard Interrupt (CTRL-C) is pressed
	pass					#Go to next line

finally:
	GPIO.cleanup()			#Make all GPIO pins low