#include <CODELAB.h>

#define RELAY_PIN 17

void setup() {
  CODELAB::begin();
  beep();
  display.clearDisplay();
  display.setCursor(0, 0);
  display.setTextSize(2);
  display.println("Ready!!");
  display.display();
  
  // เริ่มต้นกำหนดเป็น INPUT (สถานะลอยขา = ปิดสำหรับเคสไฟรั่ว)
  pinMode(RELAY_PIN, INPUT); 
}

void loop() {
  if (sw(0)) {          // กดปุ่ม
    pinMode(RELAY_PIN, OUTPUT);
    digitalWrite(RELAY_PIN, LOW); // สั่งทำงาน (Active Low)
  } else {              // ปล่อยปุ่ม
    pinMode(RELAY_PIN, INPUT); 
  }
}