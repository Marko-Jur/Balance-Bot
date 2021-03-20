#include "MotorController.h"
#include "Pin_Assignments.h"
#include "Arduino.h"

#define MAX_SPEED 200


MotorController::MotorController()
{
    motorSetup();
}

MotorController::MotorController(int enA, int enB, int in1, int in2, int in3, int in4)
    : m_enA(enA), m_enB(enB), m_in1(in1), m_in2(in2), m_in3(in3), m_in4(in4)
{
    motorSetup();
}

MotorController::~MotorController()
{

}


void MotorController::setMotorSpeed(float outputSpeed) {
    int set_speed = 0;
    int abs_error = abs(outputSpeed);
    set_speed = min(MAX_SPEED, abs_error);
    analogWrite(m_enA, set_speed);
    analogWrite(m_enB, set_speed);
}

void MotorController::output(float outputValue)
{
    
    setMotorSpeed(outputValue);
    if (outputValue > 0) {
        motorForward();
        Serial.print("Moving Forward: ");
        
    }
    else
    {
        motorReverse();
        Serial.print("Moving Backward: ");
    }
    Serial.println(outputValue);
}

void MotorController::motorForward()
{
    digitalWrite(m_in1, HIGH);
    digitalWrite(m_in2, LOW);
    digitalWrite(m_in3, LOW);
    digitalWrite(m_in4, HIGH);
}

void MotorController::motorReverse()
{
    digitalWrite(m_in1, LOW);
    digitalWrite(m_in2, HIGH);
    digitalWrite(m_in3, HIGH);
    digitalWrite(m_in4, LOW);
}

void MotorController::motorSetup()
{
    pinMode(m_enA, OUTPUT);
    pinMode(m_enB, OUTPUT);

    //Motor A pins
    pinMode(m_in1, OUTPUT);
    pinMode(m_in2, OUTPUT);

    //Motor B pins
    pinMode(m_in3, OUTPUT);
    pinMode(m_in4, OUTPUT);

    //Initial state - motor off
    digitalWrite(m_in1, LOW);
    digitalWrite(m_in2, LOW);
    digitalWrite(m_in3, LOW);
    digitalWrite(m_in4, LOW);
}