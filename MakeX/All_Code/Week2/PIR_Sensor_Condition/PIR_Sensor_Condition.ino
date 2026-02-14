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

  if (sen(1) > 2000) {   //PIR เสียบช่อง Sen(1)
    display.println("Detected");
    beep();
    analogWrite(17,255); //Turn ON LED pin17[servo(0)]
    delay(2000);
    
  } 
  else {
    display.println("Not Detected");
    analogWrite(17,0); //Turn OFF LED pin17[servo(0)]
  }

  display.display();
  delay(300);
}
