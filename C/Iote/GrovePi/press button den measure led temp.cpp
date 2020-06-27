#include "grovepi.h" 
#include "grove_dht_pro.h"
using namespace GrovePi;
using GrovePi::DHT;
using GrovePi::delay;
using GrovePi::I2CError;
int main()
{
	int button_pin = 3;
	int button_state;
	int LED_pin=4;
	int sensorPin = 2;
	float temp = 0, humidity = 0;
	DHT dht = DHT(DHT::BLUE_MODULE, sensorPin);
	try
	{
		dht.init();  
		initGrovePi();
		pinMode(button_pin, INPUT);
		pinMode(LED_pin,OUTPUT);
		while(true)
		{
			button_state = digitalRead(button_pin);
			printf("[pin %d](button state =", button_pin);
			if(button_state == 0)
			{
			digitalWrite(LED_pin,LOW);
			printf("[pin %d][LED OFF]\n",LED_pin);
			
			}
			else
			{
			digitalWrite(LED_pin,HIGH);
			printf("[pin %d][LED ON]\n",LED_pin);
		    dht.getSafeData(temp,humidity);
			printf("[temp = %.02f C][humidity = %.02f%%]\n", temp, humidity);
			delay(100);
			}
		}
	}
	catch(I2CError &error)
	{
		printf(error.detail());
		return -1;
	}	
	catch(std::runtime_error &e)
	{
		printf(e.what());
		return -2;
	}
	return 0;
}
			
			
