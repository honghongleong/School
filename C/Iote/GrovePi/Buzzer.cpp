#include "grovepi.h"
using namespace GrovePi;

int main()
{
int buzzer_pin = 8; // Buzzer is connected to digital port D8

 
try
{
 


initGrovePi(); // initialize communication
pinMode(buzzer_pin, OUTPUT); // set buzzer_pin as OUTPUT

// do indefinitely while(true)
{
 
// turn ON the buzzer for 1000 ms (1 sec)
// and put the state on the screen digitalWrite(buzzer_pin, HIGH);
printf("[pin %d][buzzer ON]\n", buzzer_pin); delay(1000);

// and then OFF for another 1000 ms (1 sec)
// and put the state on the screen digitalWrite(buzzer_pin, LOW);
printf("[pin %d][buzzer OFF]\n", buzzer_pin); delay(1000);
}
}
catch(I2CError &error)
{
printf(error.detail()); return -1;
}

return 0;
}
