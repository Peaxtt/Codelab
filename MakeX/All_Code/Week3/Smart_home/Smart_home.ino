#include <CODELAB.h>

void setup() {
  CODELAB::begin();
  beep();

  // Show message
  display.clearDisplay();
  display.setTextSize(2);
  display.setCursor(0, 0);
  display.println("Smart Home");
  display.display();
  delay(1000);
}

void loop() {
  int ldr = sen(0);   // LDR sensor (light)
  int pir = sen(1);   // PIR sensor (motion)

  // Conditions
  bool dark   = ldr > 2000;   // true = dark
  bool motion = pir > 2000;   // true = motion detected

  // Light 1: Main house light (turns on when dark)
  if (dark) {
          analogWrite(15, 255);   // light ON (pin15)
  } else {
    analogWrite(15, 0);     // light OFF
  }

  // Light 2: Motion light (only when dark + motion)
  if (dark && motion) {
    analogWrite(17, 255);   // ON motion light (pin17)
    beep();                 // beep for feedback
  } else {
    analogWrite(17, 0);     // OFF motion light
  }
}