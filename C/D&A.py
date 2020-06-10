import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Buzzer = 25
TRIG = 23
ECHO = 24
Green = 17
Red = 27
Yellow = 22
LDR = 4   

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(Green,GPIO.OUT)
GPIO.setup(Yellow, GPIO.OUT)
GPIO.setup(Red, GPIO.OUT)
GPIO.setup(Buzzer, GPIO.OUT)
GPIO.setup(LDR, GPIO.IN)


while True:
    if GPIO.input(LDR) == 0:
        print ("Fire Detected !")
        GPIO.output(Buzzer,GPIO.HIGH)
        while True:
            GPIO.output(Green,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(Green,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(Yellow,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(Yellow,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(Red,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(Red,GPIO.LOW)
 #“Add codes to blink the LEDs at 500msec and turn on Buzzer”
    else:
        GPIO.output(TRIG,True)  # generate short pulse to trigger the ultrasonic sensor.
        time.sleep(0.00001)
        GPIO.output(TRIG,False)
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150    #Calculate distance
        distance = round(distance, 2)
        print ("distance: ", distance, "cm")
        
        if distance <= 20:#distance is 0 to 20
            GPIO.output(Buzzer,GPIO.HIGH)
            GPIO.output(Green,GPIO.HIGH)
            GPIO.output(Yellow,GPIO.HIGH)
            GPIO.output(Red,GPIO.HIGH)
        elif distance <= 50:#distance is between 0 to 50
            GPIO.output(Buzzer,GPIO.LOW)
            GPIO.output(Green,GPIO.HIGH)
            GPIO.output(Yellow,GPIO.HIGH)
            GPIO.output(Red,GPIO.LOW)
        elif distance <= 80:#distance is 0 to 80
            GPIO.output(Buzzer,GPIO.LOW)
            GPIO.output(Green,GPIO.HIGH)
            GPIO.output(Yellow,GPIO.LOW)
            GPIO.output(Red,GPIO.LOW)
        else:
            GPIO.output(Buzzer,GPIO.LOW)
            GPIO.output(Green,GPIO.LOW)
            GPIO.output(Yellow,GPIO.LOW)
            GPIO.output(Red,GPIO.LOW)

