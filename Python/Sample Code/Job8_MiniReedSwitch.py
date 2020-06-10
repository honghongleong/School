#Job 8 Reed Switch Test

import RPi.GPIO as GPIO
import pygame
from time import sleep

ReedSwitchPin = 14
LED = 15
RawValue = 0

#Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(ReedSwitchPin, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

#SFX
pygame.init()
pygame.mixer.init()
Alarm = pygame.mixer.Sound("/home/pi/python_games/match1.wav")
print("Reed Switch Door Alarm ...")

try:
	while 1:
		RawValue = GPIO.input(ReedSwitchPin)
		if (RawValue == 0):
			GPIO.output(LED, True)
			Alarm.play()

		else:
			GPIO.output(LED,False)
			Alarm.stop()

		# 1 is off, 0 is activated by magnet
		print(" , RawValue:",RawValue)

except KeyboardInterrupt:
	pass

print("Exiting Reed Switch Test ...")

GPIO.cleanup()