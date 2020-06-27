#include <wiringPi.h>

int main(void)
{
	int i=0;
	
	wiringPiSetup();
	
	pinMode(28,INPUT);
	pinMode(29,INPUT);
	
	for(i=0;i<8;i++)
	{
		pinMode(i,OUTPUT);
	}
	while(1)
	{
		if(digitalRead(29)==0 && digitalRead(28)==0)
		{
			for(i=7;i>=0;i--)
			{
				digitalWrite(7-i,HIGH);
				delay(250);
			}
			for(i=0;i<8;i++)
			{
				digitalWrite(7-i,LOW);
				delay(250);
			}
		}
		else if(digitalRead(29)==1 && digitalRead(28)==0)
		{
			for(i=0;i<8;i++)
			{
				digitalWrite(7-i,HIGH);
				delay(250);
			}
			for(i=0;i<8;i++)
			{
				digitalWrite(7-i,LOW);
				delay(250);
			}
		}
		else if(digitalRead(29)==0 && digitalRead(28)==1)
		{
			for(i=0;i<8;i++)
			{
				digitalWrite(7-i,HIGH);
				delay(250);
			}
			for(i=0;i<8;i++)
			{
				digitalWrite(7-i,LOW);
				delay(250);
			}
		}
		else
		{
			for(i=0;i<8;i++)
			{
				digitalWrite(7-i,HIGH);
				delay(250);
			}
			for(i=0;i<8;i++)
			{
				digitalWrite(7-i,LOW);
				delay(250);
			}
		}
	}
}
