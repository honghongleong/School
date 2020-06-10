#Example scroll message

import RPi.GPIO as GPIO		
import time					
from time import sleep, strftime
from datetime import datetime
import Adafruit_CharLCD as LCD

#Raspberry Pi pin configuration
lcd_rs        = 27  
lcd_en        = 22  
lcd_d4        = 25 
lcd_d5        = 24 
lcd_d6        = 23 
lcd_d7        = 18 
lcd_backlight = 4  

#Define LCD column and row size for 16x2 LCD
lcd_columns = 16 
lcd_rows    = 2 

#Initialize the LCD using the pins above
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, 
                           lcd_columns, lcd_rows, lcd_backlight)   

#Write your message
title = "Don't forget!"
reminder = "Your deadline for the project is next Monday."

#Set the delay for scroll
delay = 0.3

#Write a function to scroll the message
def scroll_message(reminder,delay):
	padding=''*lcd_columns
	reminder_message = padding+reminder+''
	for i in range(len(reminder_message)):
		lcd.set_cursor(0,1)
		lcd.message(reminder_message[i:(i+lcd_columns)])
		time.sleep(delay)
		
#Scroll message right/left
def scroll(message):
	for i in range(lcd_columns-len(message)):
		time.sleep(0.5)
		lcd.move_right()
	for i in range(lcd_columns-len(message)):
		time.sleep(0.5)
		lcd.move_left()

try:
	while True:
		#Program start here
		lcd.clear()
		lcd.home()
		time.sleep(0.2)
		lcd.message(title)
		scroll(title)
		
		#Scroll message in an infinite loop
		while True:
			scroll_message(reminder,delay)
		
except KeyboardInterrupt:		
	pass						
	
finally:
	GPIO.cleanup()				

