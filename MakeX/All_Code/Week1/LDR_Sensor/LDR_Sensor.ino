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
  
void loop() {  // Loop to display the value of sen(1)
  display.clearDisplay();
  display.setCursor(0, 0);
  display.print("LDR = ");
  display.println(sen(1)); 
  display.display();
  delay(300); //Every 300ms
  if (sen(1)<500){
    analogWrite(17, 0);
  }
  else{
    analogWrite(17, 255);
  }
}
