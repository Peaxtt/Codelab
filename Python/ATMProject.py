import sys # เรา import 'sys' มาเพื่อใช้คำสั่ง 'sys.exit()' สำหรับหยุดโปรแกรม

# --- ค่าเริ่มต้นของระบบ ---
CORRECT_PASSWORD = "1234"  # ตั้งรหัสผ่านของระบบ
account_balance = 20000     # ตั้งเงินในบัญชีเริ่มต้น (เช่น 20,000)
login_attempts = 0          # ตัวนับการล็อกอินผิด
IS_LOGGED_IN = False        # สถานะการล็อกอิน (เริ่มต้นคือยังไม่ล็อกอิน)

# --- Part 1: Enter Password (ลูปการล็อกอิน) ---
# (โจทย์: "If password Incorrect 3 time then show 'Error' and Stop program")
while login_attempts < 3:
    password = input("Enter Password : ")
    
    if password == CORRECT_PASSWORD:
        print("Login Successful!")
        IS_LOGGED_IN = True
        break # ถ้าถูก ให้ออกจากลูปนี้ (ไปต่อ Part 2)
    else:
        login_attempts = login_attempts + 1
        print(f"Incorrect password. {3 - login_attempts} attempts remaining.")

# ถ้าวนลูปจนครบ 3 ครั้งแล้วยังล็อกอินไม่ได้ (IS_LOGGED_IN ยังเป็น False)
if not IS_LOGGED_IN:
    print("Error. Too many incorrect attempts. Stopping program.")
    sys.exit() # สั่งหยุดโปรแกรมทันที

# --- Part 2 & 3: Main Menu (ลูปโปรแกรมหลัก) ---
# (โจทย์: ต้องวนกลับมาหน้าเมนูได้เรื่อยๆ)
while True:
    
    # แสดงเมนูและยอดเงินคงเหลือ (ตามโจทย์ Part 1 & 2)
    print("\n--- ATM Menu ---")
    print(f"Account Balance : {account_balance} baht")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit Program") # (เพิ่ม 'Exit' เข้ามาเพื่อให้จบโปรแกรมได้)
    
    choice = input("Enter choice : ")
    
    # --- Part 2: Deposit ---
    if choice == '1':
        try:
            deposit_amount = float(input("Enter the amount to deposit : "))
            
            if deposit_amount <= 0:
                print("Amount must be positive.")
            else:
                account_balance = account_balance + deposit_amount
                # (โจทย์: "show account balance")
                print(f"Deposit successful. New Account Balance : {account_balance} baht")
                
        except ValueError:
            print("Invalid amount. Please enter a number.")
            
    # --- Part 3: Withdraw ---
    elif choice == '2':
        
        # เราจะสร้างลูป "ย่อย" ข้างในนี้
        # (โจทย์: "If the above conditions are not met, please re-enter the amount")
        while True:
            try:
                withdraw_amount = int(input("Enter the amount to withdraw : "))
                
                # ตรวจสอบเงื่อนไข 3 ข้อ (ตามโจทย์)
                
                # เงื่อนไข 1: "must be less than the account balance"
                if withdraw_amount > account_balance:
                    print("Error: Not enough money in account.")
                
                # เงื่อนไข 2: "must be greater than 100 Baht"
                elif withdraw_amount <= 100:
                    print("Error: Withdrawal amount must be greater than 100 Baht.")
                    
                # เงื่อนไข 3: "Only 100 bills and above are available"
                # (เราจะตีความว่า ต้องหารด้วย 100 ลงตัว)
                elif withdraw_amount % 100 != 0:
                    print("Error: Amount must be in multiples of 100 (100, 500, 1000).")
                    
                else:
                    # ถ้าผ่านทุกเงื่อนไข
                    # 1. หักเงิน
                    account_balance = account_balance - withdraw_amount
                    
                    # 2. คำนวณแบงค์ (ส่วนที่ยากที่สุด)
                    print("You got:")
                    
                    # เราจะใช้ "การหารเอาส่วน" (//) และ "การหารเอาเศษ" (%)
                    amount_left = withdraw_amount # สร้างตัวแปรชั่วคราว
                    
                    # แบงค์ 1000
                    bill_1000 = amount_left // 1000
                    amount_left = amount_left % 1000 # เอาเศษที่เหลือมาคิดต่อ
                    
                    # แบงค์ 500
                    bill_500 = amount_left // 500
                    amount_left = amount_left % 500 # เอาเศษที่เหลือมาคิดต่อ
                    
                    # แบงค์ 100
                    bill_100 = amount_left // 100
                    
                    # (โจทย์: "show number of Banknotes")
                    print(f"1000 : {bill_1000}")
                    print(f"500 : {bill_500}")
                    print(f"100 : {bill_100}")
                    
                    # (โจทย์: "show account balance")
                    print(f"Account Balance : {account_balance} baht")
                    
                    break # ออกจากลูป "ย่อย" (ลูป re-enter) กลับไปหน้าเมนู
                    
            except ValueError:
                print("Invalid amount. Please enter a number.")
                
    # --- จบโปรแกรม (ที่เราเพิ่มเข้ามา) ---
    elif choice == '3':
        print("Thank you for using our ATM. Goodbye!")
        break # ออกจากลูป "หลัก" (ลูป Main Menu)
        
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")