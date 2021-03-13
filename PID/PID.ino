#include "Gyroscope.h"
#include "PID.h"

float error_angle;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("Hello");
  gyroscopeSetup();
  motorSetup();
}

void loop() {
  // put your main code here, to run repeatedly:
  error_angle = getGyroAngle();
  Serial.print("Error: ");
  Serial.println(error_angle);
  motorController(error_angle);
  Serial.println();
  delay(200);
}
