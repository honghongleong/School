#Example Display data on the LCD screen

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
try:
	while True:
		dis = 12.34
		
		lcd.clear()
		
		#Print a two line message
		lcd.message(datetime.now().strftime('%b%d %H:%M:%S\n'))
		time.sleep(2.0)
		
		lcd.message('distance=%sm'%(dis))
		time.sleep(4.0)
		
		lcd.clear()
		
		lcd.set_cursor(2,1)
		lcd.message('That\'s right')
		time.sleep(2.0)
			
except KeyboardInterrupt:		
	pass						
	
finally:
	GPIO.cleanup()				

