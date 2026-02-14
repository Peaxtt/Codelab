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
  if (sw(0)==1) {         // if botton press
    servo(0, 175); // try to change degrees
  } else {              
    servo(0, 5); // try to change degrees
  }
}