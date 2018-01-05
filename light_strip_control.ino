const int lightPinDC = 2; //Turns on and off the sensor
const int lightPinIn = 14; //Reads the sensor
const int ledPin = 4; //Turns on and off the led Strip

int sensorValue = 0; //Are the lights on?
long onDuration = 0; //How long have they been on?

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(lightPinDC, OUTPUT);
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(lightPinDC, HIGH); //turn on sensor
  delay(1);
  sensorValue = analogRead(lightPinIn);

  if (sensorValue < 500) {
    digitalWrite(ledPin, HIGH);
    onDuration += 1100; //increment duration by 1.1 seconds
  }
  else {
    digitalWrite(ledPin, LOW);
    onDuration = 0;
  }

  if (onDuration > 300000) {
    digitalWrite(ledPin, LOW);
    onDuration = 0;
    while (analogRead(lightPinIn) < 500) { //loop until lights go out
      digitalWrite(lightPinDC, LOW);
      delay(1000); //check every 1 second when in this mode
      digitalWrite(lightPinDC, HIGH);
      delay(1);
    }

  }
  Serial.print("Light value: ");
  Serial.println(analogRead(lightPinIn));
  Serial.print("Time: ");
  Serial.println(onDuration);
  digitalWrite(lightPinDC, LOW); //turn off sensor
  delay(1000); //Wait one second  
}
