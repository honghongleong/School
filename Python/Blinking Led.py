import RPi.GPIO as GPIO
from time import sleep

led_pin = 12#Pin Number

GPIO.setwarnings(False)#Disable warnings

GPIO.setmode(GPIO.BCM)#Set BCM

GPIO.setup(led_pin, GPIO.OUT)#Set LED as output
while True:
    print("Led On")
    GPIO.output(led_pin, GPIO.HIGH)#Turn LED on
    sleep(.5)# Delay for 1 second
    print("Led Off")
    GPIO.output(led_pin, GPIO.LOW)#Turn LED off
    sleep(.5)# Delay for 1 second
