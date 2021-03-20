#include <Arduino.h>
#include "MotorController.h"
#include "PID.h"
#include "Pin_Assignments.h"
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

double setPoint = 0;
double sensorOutput = 0;
double pidOutput = 0;

MotorController motor_controller;
BalancePID pid = BalancePID(&sensorOutput, &pidOutput, &setPoint, 1, 0, 1);
Adafruit_BNO055 bno = Adafruit_BNO055(01, 0x28);

void setup() {
  Serial.begin(115200);
  Serial.println("HELLO WORLD!");
  if (!bno.begin()) {
    Serial.println("BNO FAILED!");
    while(1);
  }
  delay(1000);
  bno.setExtCrystalUse(true);
}

void loop() {
  sensors_event_t event;
  bno.getEvent(&event);
  Serial.print("BNO Output: ");
  Serial.println(event.orientation.y);
  sensorOutput = event.orientation.y;
  pid.Compute();
  motor_controller.output((float)pidOutput);
  delay(100);
}