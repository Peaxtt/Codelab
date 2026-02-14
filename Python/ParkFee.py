# --- Park Fee Calculator ---

# 1. ตั้งค่า "Fixed hourly rate" (อัตราค่าจอดคงที่)
# เรากำหนดตัวเลขนี้เองได้เลย
HOURLY_RATE = 40  # เช่น ชั่วโมงละ 40 บาท

# 2. สร้างลูปให้โปรแกรมทำงานซ้ำได้ (ตามโจทย์ "Option to run again or exit")
while True:
    
    # 3. รับค่าจากผู้ใช้ (ตามโจทย์ "User inputs number of hours parked")
    # และมีตัวเลือก "exit" (ตามโจทย์ "or type 'exit' to quit")
    user_input = input("Enter number of hours parked (or type 'exit' to quit): ")
    
    # 4. ตรวจสอบว่าผู้ใช้ต้องการ 'exit' หรือไม่
    # ใช้ .lower() เพื่อให้รองรับทั้ง exit, Exit, EXIT
    if user_input.lower() == 'exit':
        print("Exiting...")
        break  # สั่งให้ออกจากลูป while True
        
    # 5. ถ้าไม่ใช่ 'exit', ให้ลองคำนวณ
    # เราจะใช้ try-except ดักไว้ เผื่อผู้ใช้พิมพ์ตัวอักษรมั่วๆ ที่ไม่ใช่ตัวเลข
    try:
        # แปลงสิ่งที่รับมาเป็นตัวเลข (ใช้ float เพื่อให้เป็น 3.5 ชั่วโมงได้)
        hours = float(user_input)
        
        # คำนวณค่าจอด
        total_fee = hours * HOURLY_RATE
        
        # 6. แสดงผลลัพธ์ (ตามรูปแบบในโจทย์เป๊ะๆ)
        # "Total parking fee for 3.5 hour(s) is: xxx baht"
        print(f"Total parking fee for {hours} hour(s) is: {total_fee} baht")
        
    except ValueError:
        # จะทำงานส่วนนี้ ถ้าผู้ใช้พิมพ์ "abc" หรืออะไรก็ตามที่แปลงเป็น float ไม่ได้
        print("Invalid input! Please enter a number (like 3.5) or type 'exit'.")
        
    # พิมพ์เส้นคั่นเพื่อให้ดูง่ายเวลารันซ้ำรอบต่อไป
    print("------------------------------------------")