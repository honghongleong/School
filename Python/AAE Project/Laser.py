import RPi.GPIO as GPIO
from time import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

Laser=

GPIO.setup(Laser,GPIO.IN) # set up pin 25 as the input
GPIO.remove_event_detect(Laser)   #set defaults for event detection		
GPIO.add_event_detect(Laser,GPIO.RISING,callback=laser_a_rising_event) # register a new interrupt and its callback function
print("Waiting for event")

def laser_a_rising_event(channel):
 # this will be the function called when the laser is tripped going from high to low
 print("Function Called")
 time.sleep(.2)   # wait to check for ligitimate interupt, increase this value to decrease the sensitivity of the system
 if GPIO.input(laser_1_input):	
  #if the pin is still triggered after the sleep interval it must be a legitimate triggering
  hr  = strftime("%H",time.localtime()) #get the hour
  min = strftime("%M",time.localtime()) #get the minutes
  sec = strftime("%S",time.localtime()) #get the seconds
  print("Tripped @ ",hr,":",min,":",sec)
  exec(open('./Buzzer.py').read()
 else:
  print("False positive")
 return

try:
    while True:
        sleep(0.1)
except KeyboardInterrupt:
 exit()
finally:
    GPIO.cleanup()