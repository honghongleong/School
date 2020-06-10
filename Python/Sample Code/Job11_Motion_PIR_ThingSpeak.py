#PIR Motion Sensor
import RPi.GPIO as GPIO
import time
import datetime
import urllib2

GPIO.setwarnings(False)

#GPIO24 to PIR and GPIO23 to LED
PIR = 24
LED = 23
localmotion=50

#GPIO uses broadcom numbering (GPIO numbers)
GPIO.setmode(GPIO.BCM)

#Set PIR pin as input and LED as output
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

GPIO.output(LED, False)

api_key="XSJQR12LFV7CRNMM"
base_url="http://api.thingspeak.com/update?api_key=%s"%api_key

print("Waiting for sensor to settle")
time.sleep(5)

print("Sensor is ready")

try:
        while True:
                input_state = GPIO.input(PIR)
                if input_state == True:
                        print("Motion Detected!")
                        GPIO.output(LED, True)
                        time.sleep(1)
                        url = base_url + "&field1=%s"%(input_state)
                        print(url)
                        f = urllib2.urlopen(url)
                        print f.read()
                        f.close()

        else:
                print("Motion not Detected!")
                GPIO.output(LED, False)
                time.sleep(2)

except KeyboardInterrupt:
        pass

finally:
        GPIO.cleanup()


