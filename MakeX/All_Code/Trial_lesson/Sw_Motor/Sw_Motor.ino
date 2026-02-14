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
  if (sw(0)) { 
    motor(1, 60);
  } else {
    motor_stop(1);
  }
}