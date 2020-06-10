import RPi.GPIO as GPIO		#Import the GPIO library to use the GPIO pins of Raspberry Pi
import time					#Import the time library to provide the delays in the program

GPIO.setwarnings(False)

pir_pin = 24					#Initializing pin 23 for pir
led_pin = 23					#Initializing pin 24 for led

GPIO.setmode(GPIO.BCM)			#Using BCM numbering
GPIO.setup(pir_pin, GPIO.IN) 	#Declare the pir_pin as output pin
GPIO.setup(led_pin, GPIO.OUT) 	#Declare the led_pin pin as input pin

GPIO.output(LED, False)			#Set led to low 

print("Waiting for sensor to settle")	#Print message
time.sleep(5)					#Delay for 5 sec

print("Sensor is ready")		#Print message

try:
	while True:							#Loop will run forever
	input_state = GPIO.input(pir_pin)	#Read the pir state
	
	if input_state == True:				#Check whether the input is true		
		print("Motion Detected!")		#Print message
		GPIO.output(led_pin, True)		#Turn ON LED
		time.sleep(1)					#Delay for 1 sec

	else:
		GPIO.output(led_pin, False)		#Turn OFF LED
		time.sleep(2)					#Delay for 2 sec

except KeyboardInterrupt:		#if keyboard Interrupt (CTRL-C) is pressed
	pass						#Go to next line
	
finally:
	GPIO.cleanup()				#Make all GPIO pins low