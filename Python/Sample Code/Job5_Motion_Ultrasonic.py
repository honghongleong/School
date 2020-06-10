import RPi.GPIO as GPIO		#Import the GPIO library to use the GPIO pins of Raspberry Pi
import time					#Import the time library to provide the delays in the program

GPIO.setwarnings(False)

TRIG_pin = 23					#Initializing pin 23 for TRIG
ECHO_pin = 24					#Initializing pin 24 for ECHO

GPIO.setmode(GPIO.BCM)			#Using BCM numbering
GPIO.setup(TRIG_pin, GPIO.OUT) 	#Declare the TRIG pin as output pin
GPIO.setup(ECHO_pin, GPIO.IN) 	#Declare the ECHO pin as input pin

try:
	while True:										#Loop will run forever
		GPIO.output(TRIG_pin, False)				#Set TRIG as low. Wait for the sensor to settle
		print("Waiting for sensor to settle")
		time.sleep(2)								#Delay for 2 sec

		GPIO.output(TRIG_pin, True)					#Set 10us TRIG Pulse as high
		time.sleep(1)								#Delay for 1 sec
		GPIO.output(TRIG_pin, False)				#Set TRIG as low

		while GPIO.input(ECHO_pin) == 0:			#Check whether the ECHO_pin is low
			pulse_start = time.time()				#Record the pulse_start time

		while GPIO.input(ECHO_pin) == 1:			#Check whether the ECHO_pin is high
			pulse_end=time.time()					#Record the pulse_end time

		pulse_duration = pulse_end - pulse_start	#Calculate the pulse_duration

		distance = pulse_duration*17150				#Calculate the distance
		distance = round(distance, 2)				#Round the distance to 2 decimal place

		if(distance > 2 and distance < 400):		#Check if distance between 2 to 400
			print("Distance:", distance - 0.5, "cm") #Print distance with 0.5cm calibration
			
		else:
			print("Out of Range")					#Print out of range

except KeyboardInterrupt:		#if keyboard Interrupt (CTRL-C) is pressed
	pass						#Go to next line
	
finally:
	GPIO.cleanup()				#Make all GPIO pins low