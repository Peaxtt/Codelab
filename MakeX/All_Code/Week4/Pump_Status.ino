#define RELAY_PIN 17 // Tell the board that this pin will be used to send signals

void setup() {
  pinMode(RELAY_PIN, OUTPUT);
}

void loop() {
  // Send ON signal to the relay
  digitalWrite(RELAY_PIN, HIGH);
  delay(2000); // Wait 2 seconds

  // Send OFF signal to the relay
  digitalWrite(RELAY_PIN, LOW);
  delay(2000); // Wait 2 seconds
}