#include <CODELAB.h>

#define LED_PIN 17
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
  if (sw(0)==1) {         // if botton press
    digitalWrite(LED_PIN, HIGH);
    motor(1, 60);
  } else {              
    digitalWrite(LED_PIN, LOW); 
    motor_stop(1);
  }
}