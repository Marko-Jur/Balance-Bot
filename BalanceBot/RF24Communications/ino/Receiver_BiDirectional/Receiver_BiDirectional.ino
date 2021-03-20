#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
RF24 radio(7, 8); // CE, CSN

const byte addresses[][6] = {"00001", "00002"};
const int NUM_DATA_POINTS = 32;
const char recvData[NUM_DATA_POINTS] = {};
const char sendData[NUM_DATA_POINTS] = "Message from Wall-E.............";

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.maskIRQ(1,1,0);
  radio.setPALevel(RF24_PA_MIN);
  radio.openWritingPipe(addresses[0]);
  radio.openReadingPipe(1, addresses[1]);
  radio.startListening();
  attachInterrupt(digitalPinToInterrupt(3), doStuff, FALLING);
}

void loop() {
}

void doStuff(){
  while (radio.available()) {
    radio.read(&recvData, sizeof(recvData));
    Serial.println(recvData);
  }
  
  delay(25);
  radio.stopListening();

  radio.write(&sendData, sizeof(sendData));

  delay(25);
  radio.startListening();
}
