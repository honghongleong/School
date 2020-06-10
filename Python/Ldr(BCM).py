import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
delayt = .1 
value = 0 # this variable will be used to store the ldr value
ldr = 22 #ldr is connected with pin number 7
led = 12 #led is connected with pin number 11
GPIO.setup(led, GPIO.OUT) # as led is an output device so that’s why we set it to output.
GPIO.output(led, False) # keep led off by default 
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
        if ( value <= 10000 ):
                print("Lights are ON")
                GPIO.output(led, True)
        if (value > 10000):
                print("Lights are False")
                GPIO.output(led, False)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
