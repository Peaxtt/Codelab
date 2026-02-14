#include <CODELAB.h>

void setup() {
  CODELAB::begin();
  beep();
}

void loop() {
  int s1 = sw(1);   // Read switch 1
  int s2 = sw(2);   // Read switch 2

  // AND: both must be true (pressed)
  if (s1 == 1 && s2 == 1) {
    analogWrite(17, 255);  // Turn ON LED
  } else {
    analogWrite(17, 0);    // Turn OFF LED
  }
}
