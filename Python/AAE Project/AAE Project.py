import RPi.GPIO as GPIO
from time import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
delayt=0.1
value=0
ldr=4
button=6
led=5

GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(led,GPIO.OUT)

def rc_time (ldr):
    count = 0

    #Output on the pin for
    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, False)
    sleep(delayt)

    #Change the pin back to input
    GPIO.setup(ldr, GPIO.IN)

    #Count until the pin goes high
    while (GPIO.input(ldr) == 0):
        count += 1

    return count
try:
    complete=False
    input_button=GPIO.input(button)
    while complete == False:
        value = rc_time(ldr)
        print("Ldr Value:{}".format(value))
        if ( value <= 10000 ):#don't cover
                print("Lights are on")
                
        elif (value > 10000):#cover
            print("Lights are False")
        #exec(open('./ldr.py').read())
        sleep(1)
        if input_button == False:#Break/Stop from running
            complete=True
#help when interrut happens(KB)
except KeyboardInterrupt:
    print("help")
finally:
    GPIO.cleanup()