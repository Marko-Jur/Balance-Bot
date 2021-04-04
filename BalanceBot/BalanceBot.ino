#include <Arduino.h>
#include "MotorController.h"
#include "PID.h"
#include "Pin_Assignments.h"
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include "RC_Transmitter.h"

void(* resetFunc) (void) = 0;

double setPoint = 0;
double sensorOutput = 0;
double pidOutput = 0;
int channel_values[9] = {};



MotorController motor_controller;
                                                                //kp,ki,kd
BalancePID pid = BalancePID(&sensorOutput, &pidOutput, &setPoint, 8.0, 0.0, 400.0);
Adafruit_BNO055 bno = Adafruit_BNO055(01, 0x28);

void setup() {
  Serial.begin(115200);
//  setupRc();
//  rcReader(channel_values);
  if (!bno.begin()) {
    Serial.println("BNO FAILED!");
    while(1);
  }
  delay(1000);
  bno.setExtCrystalUse(true);
//  Serial.println(channel_values[3] - 1000.0);
//  while (channel_values[3] - 1000.0 < 100.0) {
//    rcReader(channel_values);
//    delay(100);
//  }
  delay(2000);
}

void loop() {
  sensors_event_t event;
  bno.getEvent(&event);
  sensorOutput = event.orientation.z;
//  rcReader(channel_values);
//  Serial.println(channel_values[3] - 1000.0);
//  if (channel_values[3] - 1000.0 < 100.0) {
//    resetFunc();
//  }
  setPoint = ((double)channel_values[0] - 1500.0) / 250.0;
  Serial.println(pidOutput);
  pid.Compute();
  motor_controller.output((float)pidOutput);
}
