import RPi.GPIO as GPIO

#Pin Number
btn_pin = 4
led_pin = 12

GPIO.setwarnings(False)#Disable warnings
GPIO.setmode(GPIO.BCM)#Set BCM
GPIO.setup(btn_pin, GPIO.IN)#Input
GPIO.setup(led_pin, GPIO.OUT)#Output

#If button is pushed, light up LED
try:
    while True:
        if GPIO.input(btn_pin):
            GPIO.output(led_pin, GPIO.LOW)
        else:
            GPIO.output(led_pin, GPIO.HIGH)

#When you press ctrl+c, this will be called
finally:
    GPIO.cleanup()
