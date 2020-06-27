#include "grovepi.h" 
using namespace GrovePi;
int main()
{
	int light_sensor_pin=0;
	int LED_pin = 4;
	int threshold = 10;
	int sensor_value;
	float resistance;
	try
	{
		initGrovePi();
		pinMode(light_sensor_pin,INPUT);
		pinMode(LED_pin,OUTPUT);
		while(true)
		{
			sensor_value = analogRead(light_sensor_pin);
			resistance = (float)(1023 - sensor_value)*10/sensor_value;
			printf("[ledpin %d][light pin %d][sensor value = %d][resistance = %.2f]",LED_pin,light_sensor_pin,sensor_value,resistance);
			if(resistance>threshold)
			{
				digitalWrite(LED_pin,HIGH);
				printf("[led ON]\n");
			}
			else
			{
				digitalWrite(LED_pin,LOW);
				printf("[led OFF]\n");
			}
			delay(200);
		}
	}
		catch(I2CError &error)
	{
		printf(error.detail());
		return -1;
	}
	return 0;
}
