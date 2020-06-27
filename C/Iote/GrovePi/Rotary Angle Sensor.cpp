#include "grovepi.h"
using namespace GrovePi;

int main()
{
int potentiometer_pin = 0; // potentiometer is connected to A0 port int LED_pin = 5; // LED is connected to D5 port

int adc_ref = 5; // reference voltage of ADC is 5V
int grove_ref_vcc = 5; // Grove's reference voltage is 5V, regularly int full_angle = 300; // max turning angle for the potentiomater

 
try
{
 


initGrovePi(); pinMode(potentiometer_pin, INPUT); pinMode(LED_pin, OUTPUT);

// do this indefinitely while(true)
{
 
// start reading potentiometer's values
int sensor_value = analogRead(potentiometer_pin);
// calculate voltage
float voltage = (float)(sensor_value) * adc_ref / 1023;

// calculate rotation in degrees (0 to 300)
float degrees = voltage * full_angle / grove_ref_vcc;

// and calculate brightness for the LED
// basically we map values 0->300 to 0->255 int brightness = int(degrees / full_angle * 255);
float percentage_brightness = 100 * float(brightness) / 255;

// and give a PWM output to the LED analogWrite(LED_pin, brightness);

// and display status data onto the terminal
printf("[rotar pin %d][led pin %d][sensor value = %d][voltage =
%.2f][degrees = %.1f][brightness = %.2f%%]\n", potentiometer_pin, LED_pin, sensor_value, voltage, degrees, percentage_brightness);
}
}
catch(I2CError &error)
{
printf(error.detail()); return -1;
}
 

// wait 20 ms for the next reading
// this equates to a rate of 50Hz
// so there are 50 reads / second -> more than enough delay(20);

return 0;
}
