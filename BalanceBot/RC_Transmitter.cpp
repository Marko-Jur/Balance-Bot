//Contains all files for PPM receiver 
#import <Arduino.h>
#include "Pin_Assignments.h"
#include "RC_Transmitter.h" 

//Array for values:
unsigned long int a,b,c;
int x[15],ch1[15],ch[10],i;
//Throttle - CH[4]
//Right Lateral - CH[2]
//Switch A - CH[6]
//Switch B - CH[7]
//Switch C - CH[8]


/*Function: RC Setup
 *Author: Marko Jurisic
 *Input Parameters: None
 *Output Parameters: None
 *
 *Purpose: Sets up the receiver
 * 
 */
void setupRc(){

 //Setting up the motors
 pinMode(2, INPUT_PULLUP);
 attachInterrupt(digitalPinToInterrupt(2), read_me, FALLING);
  // enabling interrupt at pin 2

  
}

/*Function: RC Reader
 *Author: Marko Jurisic
 *Input Parameters: An array of steering values
 *Output Parameters: Modifies the input array with values from the transmitter
 *
 *Purpose: Getting values from the transmitter to steer Scorpion
 * 
 */

void rcReader(int channel_values[9]){
  read_rc();

  channel_values[0] = ch[4]; //Throttle
  channel_values[1] = ch[2]; //Right Lateral
  channel_values[2] = ch[6]; //Switch A
  channel_values[3] = ch[7]; //Switch B
  channel_values[4] = ch[8]; //Switch C



}


void read_me()  {
 //this code reads value from RC reciever from PPM pin (Pin 2 or 3)
 //this code gives channel values from 0-1000 values
 //    -: ABHILASH :-    //
a=micros(); //store time value a when pin value falling
c=a-b;      //calculating time inbetween two peaks
b=a;//
x[i]=c;     //storing 15 value in array
i=i+1;

if(i==15){
  for(int j=0;j<15;j++){
    ch1[j]=x[j];
    delay(1);
    }
             i=0;}}//copy store all values from temporary array another array after 15 reading 

void read_rc(){
int i,j,k=0;
  for(k=14;k>-1;k--){//k = 14
    if(ch1[k]>10000){
      j=k;
      delay(1);
      }}//detecting separation space 10000us in that another array //delay
                         
  for(i=1;i<=8;i++){ //i = 6
    ch[i]=(ch1[i]);
    delay(1);
    }}
    //assign 6 channel values after separation space
