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
  display.clearDisplay();
  display.setCursor(0, 0);

  display.print("UltraSn = ");
  display.println(sen(0));   // แสดงค่าที่อ่านได้จากช่อง sen(0)

  display.display();
  delay(300);
}