#include "grovepi.h" 
#include "grove_dht_pro.h"
using GrovePi::DHT;
using GrovePi::delay;
using GrovePi::I2CError;
int main()
{
	int sensorPin = 2;
	float temp = 0, humidity = 0;
	DHT dht = DHT(DHT::BLUE_MODULE, sensorPin);
	try
	{
		dht.init();  
		while(true)
		{
			dht.getSafeData(temp,humidity);
			printf("[temp = %.02f C][humidity = %.02f%%]\n", temp, humidity);
			delay(100);
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
