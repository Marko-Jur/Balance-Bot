/*
Function: Motor Controller
Author: Harmandeep Singh Dubb
Input Parameters: error_angle
Output Parameters: None

Purpose: *Initializes balance bot with a taget vertical position, and then the balance bot maintains that position


*/

#ifndef _MOTORCONTROLLER_H
#define _MOTORCONTROLLER_H

//Function declarations
void motorController(float error_angle);
void motorSetup();
void motorForward();
void motorReverse();
void set_motor_speed(float error_speed);

#endif
