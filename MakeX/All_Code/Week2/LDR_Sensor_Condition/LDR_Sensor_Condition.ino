#include <CODELAB.h>

void setup() {
  CODELAB::begin();
  beep();
  display.clearDisplay();
  display.setCursor(0, 0);
  display.setTextSize(3);
  display.println("Ready!!");
  display.display();
}

void loop() {
  display.clearDisplay();
  display.setCursor(0, 0);

  if (sen(0) > 2000) {   //LDR เสียบช่อง Sen(1)
    display.println("Dark");
    analogWrite(15,255); // Turn ON Relay pin15[servo(2)]
    beep(); // Beep เพื่อเช็ค
  } 
  else {
    display.println("Bright");
    analogWrite(15,0); // Turn OFF Relay pin15[servo(2)]
  }

  display.display();
  delay(300);
}
