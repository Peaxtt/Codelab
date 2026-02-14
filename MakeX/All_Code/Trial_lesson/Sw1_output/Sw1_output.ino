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

void loop() {  // Loop to display the value of sw(1)
  display.clearDisplay();
  display.setCursor(0, 0);
  display.print("SW(1) = ");
  display.println(sw(1)); 
  display.display();
  delay(300); //Every 300ms
  }
