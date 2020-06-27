#include "grovepi.h"
using namespace GrovePi;

int main()
{
int pin = 4; // connected to digital port 4 (D4) int incoming; // variable to hold the data

 
try
{
 


initGrovePi(); // initialize communication

// do this indefinitely while(true)
{
 
// read the processed data from the GrovePi incoming = ultrasonicRead(pin);

// display it
printf("[pin %d][ultrasonic read = %d cm]\n", pin, incoming);

// and wait 50 ms for the ultrasonic sensor to get a new reading delay(50);
}
}
catch(I2CError &error)
{
printf(error.detail()); return -1;
}

return 0;
}
