#include <CODELAB.h>

void setup() {
  CODELAB::begin();
  beep();
  display.clearDisplay();
  display.setCursor(0, 0);
  display.setTextSize(2);
  display.println("Ready!!");
  display.display();
}

void loop() {
  int moisture_val = sen(0);  // อ่านค่า moisture sensor จากช่อง sen(0)
  display.clearDisplay();
  display.setCursor(0, 0);
  display.print("Val = ");
  display.println(moisture_val);   
  if (moisture_val > 2000){   // Low Value : High moisture
    display.setCursor(0, 25);
    analogWrite(17, 1);   // Relay on Pump on
    display.print("pump on"); //show on display "pump on"
  } 
  else {                      // High Value : Low moisture
    display.setCursor(0, 25);
    analogWrite(17, 0);   // Relay off Pump off
    display.print("pump off"); //show on display "pump off"
  }
  display.display();
  delay(300);
}

void waterPlant() {
  // Put your code here
  // Example: turn pump on
}

void waterThePlant() {
  analogWrite(17, 1);     // Relay on Pump on
  display.print("pump on");
  delay(2000);              // Wait for 2 seconds
  analogWrite(17, 0);     // Relay off Pump off
  display.print("pump off");
}


void loop() {

  waterThePlant();
  
  delay(10000); // Wait 10 seconds before watering again
}


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
