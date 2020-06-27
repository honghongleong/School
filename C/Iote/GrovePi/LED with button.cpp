#include "grovepi.h"
using namespace GrovePi;
int main()
{
	int button_pin = 3;
	int button_state;
	int LED_pin=4;
	
	try
	{
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
		
			}
		}
	}
	catch(I2CError &error)
	{
		printf(error.detail());
		return -1;
	}
	return 0;
}
