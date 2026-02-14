// if (raining) {
//   takeUmbrella();
// }
// ////
// if (homeworkDone) {
//    playGame(); 
// }
// ////
// if (hungry) {
//    eat(); 
// }

// //////////////////////////////

#include <CODELAB.h>

void setup() {
  CODELAB::begin();
  display.clearDisplay();
}

void loop() {
  if (sw(0)) { // ถ้ากดปุ่ม0
    display.clearDisplay();
    display.println("Button Pressed!");
    display.display();
  } else { // ถ้าไม่กด
    display.clearDisplay();
    display.println("Not Pressed");
    display.display();
  }
}