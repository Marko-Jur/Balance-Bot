/*
Function: "PID" Motor Controller
Author: Harmandeep Singh Dubb
Date: February 27, 2021
*
Purpose: Create a PID controller for a self balancing robot. The robot is to maintain a vertical position
Input Parameters: Angle error from the vertical position
Output Parameters: None
*/

#include "PID.h"
#include "Pin_Assignments.h"

#define MAX_SPEED 240

void motorSetup()
{
    
    pinMode(enA, OUTPUT);
    pinMode(enB, OUTPUT);

    //Motor A pins
    pinMode(in1, OUTPUT);
    pinMode(in2, OUTPUT);

    //Motor B pins
    pinMode(in3, OUTPUT);
    pinMode(in4, OUTPUT);

    //Initial state - motor off
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
    digitalWrite(in3, LOW);
    digitalWrite(in4, LOW);
}

void PIDsetup(){
    int prev_time = 0;
    float prev_error_angle = 0; 
    
    //PID Constants
    float kP = 1.0;
    float kI = 1.0;
    float kD = 1.0;
}

void motorController(float error_angle)
{
    //elaspsed time between PID loops
    int current_time = millis();

    int elapsed_time = current_time - prev_time; 

    prev_time = current_time;

    //difference in error angle 
    float diff_error_angle = error_angle - prev_error_angle;

    prev_error_angle = error_angle; 

    //Two cases needed for forward movement and reverse movement
    if (error_angle > 0)
    {
        motorForward();
    }
    else
    {
        motorReverse();
    }

    //P:instanteneousError
    float p_error_speed = error_angle * kP;

    //D:rateOFError
    float d_error_speed = (diff_error_angle)/elapsed_time*kD;

    //I:cumulativeError
    float i_error_speed = i_error_speed + (error_angle*elapsed_time)*kI;

    float error_speed =  p_error_speed + d_error_speed + i_error_speed;

    set_motor_speed(error_speed);

}

void motorForward(){
  digitalWrite(in1,HIGH);
  digitalWrite(in2,LOW);
  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW);
}

void motorReverse(){
  digitalWrite(in1,LOW);
  digitalWrite(in2,HIGH);
  digitalWrite(in3,LOW);
  digitalWrite(in4,HIGH);
}

void set_motor_speed(float error_speed){
  
  int set_speed = 0
  
  if(abs(error_speed) > MAX_SPEED){
    set_speed = MAX_SPEED;
  }else{
    set_speed = (int) abs(error_speed);
  }

  analogWrite(enA,set_speed);
  analogWrite(enB,set_speed);
}
