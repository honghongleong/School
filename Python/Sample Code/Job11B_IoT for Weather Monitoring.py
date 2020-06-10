#Read the data temperature and humidity and send to the cloud

import RPi.GPIO as GPIO
import dht11
import time
import datetime
import urllib.request

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using GPIO4
instance = dht11.DHT11(pin = 4)

api_key = "QVPDKR95FTTV800J"	#Enter your API key here
base_url = "http://api.thingspeak.com/update?api_key=%s" % api_key	#URL where we will send the data

try:
	while True:
		result = instance.read()
		if result.is_valid():
			print("Last valid input: " + str(datetime.datetime.now()))
			print("Temperature: %d C" % result.temperature)
			print("Humidity: %d %%" % result.humidity)
		
			humidity= '%.2f' % result.humidity
			temperature= '%.2f' % result.temperature

			#Sending the data to thingspeak
			url = base_url + "&field1=%s&field2=%s" % (temperature, humidity)
			print(url)
			conn = urllib.request.urlopen(url)
			print (conn.read())
			conn.close()	#Closing the connection
	
		else:
			print("error")
			
		time.sleep(2)
		
except KeyboardInterrupt:		
	pass						
	
finally:
	GPIO.cleanup()				

