#include <CODELAB.h>

void setup() {
  CODELAB::begin();
  beep();
}

void loop() {
  int s1 = sw(1);

  // NOT: reverse the result
  if (!s1) {                // If NOT pressed
    analogWrite(17, 255);   // Turn ON LED
  } else {                  // If pressed
    analogWrite(17, 0);     // Turn OFF LED
  }
}
