#include "grovepi.h"
using namespace GrovePi;

int main()
{
int relay_pin = 4; // Relay is connected to digital port D4

 
try
{
 


initGrovePi(); // initialize communication pinMode(relay_pin, OUTPUT); // set relay_pin as OUTPUT

// do this indefinitely while(true)
{
 
// turn it ON digitalWrite(relay_pin, HIGH);
printf("[pin %d][relay ON]\n", relay_pin); delay(5000); // for 5 seconds
// and turn it OFF digitalWrite(relay_pin, LOW);
printf("[pin %d][relay OFF]\n", relay_pin);

delay(5000); // for 5 seconds
}
}
catch(I2CError &error)
{
printf(error.detail()); return -1;
}

return 0;
}
