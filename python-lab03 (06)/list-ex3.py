A =[]
B = []
C = []
total = 0
print(f"โปรแกรมคำนวณสินค้า")
print(f"กด q เพื่อสรุป")
while True:
    print(f"กรอกชื่อสินค้า (กรอก Q เพื่อสรุปยอด ) : ")
    name = input()
    if name.lower() == 'q':
        break
    try:
         B1 = float(input(f"ราคา : "))
         C1 = float(input(f"จำนวนสินค้า : "))
    except ValueError:
        print(f"กรอกตัวเลข!!!!!")
        continue
    A.append(name)
    B.append(B1)
    C.append(C1)
    print(A)
    print(B)
    print(C)
for i in range(len(A)):
    sum = B[i]*C[i]
    total = total + sum
    print(f" {A[i]} x {B[i]} x {C[i]} = {B[i]*C[i]} บาท")
print(f"ยอดรวมคือ {total}")
D = float(input(f"กรอกจำนวนเงินที่ได้รับ : "))
total1 = D - total
print(f"เงินทอน{total1}")
if (total >= 5000):
 print(f"โปรโมชั่นลูกค้าshopเกิน10000บาท!!!!! รับไปเลย บัตรส่วนลด 5 % ไปใช้ในครั้งถัดไป")