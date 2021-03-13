#ifndef _GYROSCOPE_H
#define _GYROSCOPE_H
#define BNO055_SAMPLERATE_DELAY_MS (100)
//Function declarations
void displaySensorDetails();
void displaySensorStatus();
void displayCalStatus();
float getGyroAngle();
void gyroscopeSetup(void);

#endif