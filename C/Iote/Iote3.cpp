#include <wiringPi.h>

int main(void)
{
	int i=0;
	
	wiringPiSetup();
	
	for(i=0;i<8;i++)
	{
		pinMode(i,OUTPUT);
	}
	while(1)
	{
		for(i=0;i<8;i++)
			{
				digitalWrite(i,HIGH);
				delay(250);
			}
			for(i=7;i>=0;i--)
			{
				digitalWrite(i,LOW);
				delay(250);
			}
		}
	}
