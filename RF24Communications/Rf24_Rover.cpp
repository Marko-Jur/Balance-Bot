/*  RF Communications
 *  
 *  Created by: Mackenzie Mar
 *  Date: 20th February 2021
 *  Purpose: 
 */

#include "Wall-E_Libraries.h"
#include "Pin_Assignments.h"
#include "Rf24_Rover.h"

RF24 radio(7, 8); // CE, CSN
const byte addresses[][6] = {"00001", "00002"};
const char recvData[NUM_DATA_POINTS] = {};
// const char sendData[NUM_DATA_POINTS] = "Message from Wall-E.............";//debugging
const char sendData[NUM_DATA_POINTS] = {};

void setupRoverTranceiver()
{
  Serial.begin(9600);
  radio.begin();
  radio.maskIRQ(1, 1, 0);
  radio.setPALevel(RF24_PA_MIN);
  radio.openWritingPipe(addresses[0]);
  radio.openReadingPipe(1, addresses[1]);
  radio.startListening();
  attachInterrupt(digitalPinToInterrupt(3), roverListen, FALLING);
}

void roverListen()
{
  while (radio.available())
  {
    radio.read(&recvData, sizeof(recvData));
    // Serial.println(recvData);//debugging
  }
}

void roverSend()
{
  delay(25);
  radio.stopListening();

  //TODO replace with reading data from WallE gps
  //TODO add newline char ot end of string for ralph
  radio.write(&sendData, sizeof(sendData));

  delay(25);
  radio.startListening();
}

float[3] GetRoverData()
{
  float[3] data;
  int sum = 0;
  for(int i = 0; i < recvData.Count(); i++)
  {
      if (recvData[i] == ",") {
          count++;
          float[count - 3] = sum;
          sum = 0;
          break;
      }
      
  }

  return data;
}