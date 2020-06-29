import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
delayt = 0.5 
value = 0 # this variable will be used to store the ldr value
ldr = 4 #ldr is connected with pin number 21
def rc_time (ldr):
    count = 0

    #Output on the pin for
    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, False)
    time.sleep(delayt)

    #Change the pin back to input
    GPIO.setup(ldr, GPIO.IN)

    #Count until the pin goes high
    while (GPIO.input(ldr) == 0):
        count += 1

    return count


#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    while True:
        value = rc_time(ldr)
        print("Ldr Value:{}".format(value))
        if ( value <= 10000 ):#don't cover
                print("Lights are on")
                
        if (value > 10000):#cover
                print("Lights are False")
                
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()