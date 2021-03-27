/* Pin Assignments
 *  
 *  Created by: Ashwin Guru Prasad
 *  Date: 27th December 2020
 *  Purpose: Contains all pin references for Wall-E autonomous driving code
 */

#ifndef _PINASSIGNMENTS_H    
#define _PINASSIGNMENTS_H    

 //Gyroscope Assignments (already handled in code):
 // A4 -> SDA
 // A5 -> SCL
 // 5V -> Vin
 // GND -> GND
 
 //NRF24L01 Assignments:
 //Vin 3.3V
 //GND Ground
 //MOSI 11
 //MISO 12
 //SCK 13
 #define CE 9 //old pin assignments from wall-e mission controller
 #define CSN 10 //old pin assignments from wall-e mission controller
 
 
 //Motor Pins:
 #define RIGHT_MOTOR_A 4
 #define RIGHT_MOTOR_B 5
 #define RIGHT_MOTOR_ENABLE 3
 #define LEFT_MOTOR_A 7
 #define LEFT_MOTOR_B 8
 #define LEFT_MOTOR_ENABLE 9


#endif
