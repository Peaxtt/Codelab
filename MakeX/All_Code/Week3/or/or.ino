#include <CODELAB.h>

void setup() {
  CODELAB::begin();
  beep();
}

void loop() {
  int s1 = sw(1);
  int s2 = sw(2);

  // OR: at least one is true
  if (s1 == 1 || s2 == 1) {
    analogWrite(17, 255);  // Turn ON LED
  } else {
    analogWrite(17, 0);    // Turn OFF LED
  }
}
