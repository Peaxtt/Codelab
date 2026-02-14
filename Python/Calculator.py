# 1. สร้างฟังก์ชัน (ตามโจทย์สั่ง)
# น้องอาจจะตั้งชื่อตัวแปรตามที่ถนัด
def calculator(num1, num2, choice):
    if choice == '1':
        awnser = num1 + num2
        sign = '+'
    elif choice == '2':
        awnser = num1 - num2
        sign = '-'
    elif choice == '3':
        awnser = num1 * num2
        sign = '*'
    elif choice == '4':
        awnser = num1 / num2 # (น้องอาจจะยังไม่กันหารด้วย 0 เหมือนเดิม)
        sign = '/'
        
    # คืนค่า 2 อย่างออกไป
    return awnser, sign

# 2. สร้างลูป (ตามโจทย์สั่ง)

# ใช้ while True เพื่อให้มันวนไปเรื่อยๆ
while True:
    
    # แสดงเมนู
    print("Select operation:\nadd")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    # 3. รับตัวเลือก
    # และเช็ก 'exit' (ตามโจทย์สั่ง)
    choice = input("Enter choice (1-4) หรือพิมพ์ 'exit' เพื่อออก : ")
    
    if choice == 'exit':
        print("Exiting...")
        break # สั่งให้หยุดลูป
        
    # 4. รับตัวเลข
    # (น้องถนัดใช้ float)
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # 5. เรียกใช้ฟังก์ชันที่สร้างไว้
    # ฟังก์ชันคืนค่า 2 อย่าง ก็ต้องรับ 2 ตัว
    final_awnser, final_sign = calculator(num1, num2, choice)
    
    # 6. พิมพ์คำตอบ
    # (ใช้ f-string เหมือนในโจทย์เป๊ะๆ)
    print(f"Result: {num1} {final_sign} {num2} = {final_awnser}")
    
    print("--------------------") # เพิ่มคั่นไว้ให้ดูง่าย