void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

char startMarker = '<';
char endMarker = '>';
bool shouldRead = false;
String incomingData = "";

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    byte incomingByte = Serial.read();
    char incomingChar = (char) incomingByte;
    
    if (incomingChar == startMarker) {
      shouldRead = true;
      incomingData = "";
    } else if (incomingChar == endMarker) {
      shouldRead = false;
      Serial.println(incomingData);
      incomingData = "";
    } else if (shouldRead) {
      incomingData += String(incomingChar);
    }
    // incomingData is string: "##,##,##,##,##"
  }
}
