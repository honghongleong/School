#include "grovepi.h"
using namespace GrovePi;
int main()
{
	int button_pin = 3;
	int button_state;
	try
	{
		initGrovePi();
		pinMode(button_pin, INPUT);
		while(true)
		{
			button_state = digitalRead(button_pin);
			printf("[pin %d](button state =", button_pin);
			if(button_state == 0)
				printf("not pressed\n");
			else
			    printf("pressed\n");
			delay(100);
		}
	}
	catch(I2CError &error)
	{
		printf(error.detail());
		return -1;
	}
	return 0;
}
