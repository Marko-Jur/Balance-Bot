/*  RF Communications
 *  
 *  Created by: Mackenzie Mar
 *  Date: 20th February 2021
 *  Purpose: 
 */

#include "Wall-E_Libraries.h"
#include "Pin_Assignments.h"
#include "Rf24_Command.h"

RF24 radio(7, 8); // CE, CSN

const byte addresses[][6] = {"00001", "00002"};
const char sendData[NUM_DATA_POINTS] = "Message from command............";
const char recvData[NUM_DATA_POINTS] = {};
RF24 radio(7, 8); // CE, CSN

void setupCommandTranceiver()
{
  Serial.begin(9600);
  radio.begin();
  radio.openWritingPipe(addresses[1]);
  radio.openReadingPipe(1, addresses[0]);
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();
}

void commandListen()
{
  delay(25);
  radio.startListening();

  while (radio.available())
  {
    radio.read(&recvData, sizeof(recvData));
    //Serial.println(recvData); debugging
  }

  delay(25);
  radio.stopListening();
}

void commandSend(int data[NUM_DATA_POINTS])
{
  delay(25);
  radio.write(&sendData, sizeof(sendData));
}