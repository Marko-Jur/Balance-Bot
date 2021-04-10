void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
//  Serial.println("Hello World");
}

int count = 0;
int periodBetUpdate = 500;

void loop() {
  // Send bot values to serial monitor at regular rate
  Serial.println("2,30,45,55,10,25,3,1,8,2,3,4");
  delay(periodBetUpdate);
}
