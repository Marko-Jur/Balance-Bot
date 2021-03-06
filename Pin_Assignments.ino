/* Pin Assignments
 *  
 *  Created by: Ashwin Guru Prasad
 *  Date: 27th December 2020
 *  Purpose: Contains all pin references for Wall-E autonomous driving code
 */

#ifndef _PINASSIGNMENTS_H    
#define _PINASSIGNMENTS_H    

 //Gyroscope Assignments:
 
 //need to figure out gyroscope pin assignments

 
 //NRF24L01 Assignments:
//Vin 3.3V
 //GND Ground
 //MOSI 11
 //MISO 12
 //SCK 13
 #define CE 9 //old pin assignments from wall-e mission controller
 #define CSN 10 //old pin assignments from wall-e mission controller
 
 
 //Motor Pins:
 #define RIGHT_MOTOR_A //pin value
 #define RIGHT_MOTOR_B //pin value
 #define RIGHT_MOTOR_ENABLE //pin value

 #define LEFT_MOTOR_A //pin value
 #define LEFT_MOTOR_B //pin value
 #define LEFT_MOTOR_ENABLE //pin value


#endif
