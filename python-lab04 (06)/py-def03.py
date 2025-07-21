#ส่วนที่ 1: เก็บฟังก์ชันที่ใช้บ่อยๆ
def add_numbers(a, b):
    sum = a + b
    return sum

#ส่วนที่ 2: ติดต่อข้อมูลกับผู้ใช้
num = (float(input(f"กรุณาใส่ตัวเลขแรก : ")))
num2 = (float(input(f"กรุณาใส่ตัวเลขที่สอง : ")))
result = add_numbers(num, num2) #global variable
print(f"ผลลัพธ์การบวกของ: {num} + {num2} = {result}")