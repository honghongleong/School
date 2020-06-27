#include "grovepi.h"
using namespace GrovePi;
int main()
{
	int LED_pin=4;
	
	try
	{
		initGrovePi();
		pinMode(LED_pin,OUTPUT);
		delay(1000);
		
		while(true)
		{
			digitalWrite(LED_pin,HIGH);
			printf("[pin %d][LED ON]\n",LED_pin);
			delay(1000);
			
			digitalWrite(LED_pin,LOW);
			printf("[pin %d][LED OFF]\n",LED_pin);
			delay(1000);
		}
	}
	catch(I2CError &error)
	{
		printf(error.detail());
		return -1;
	}
	return 0;
}
