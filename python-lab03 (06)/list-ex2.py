A =[] #ชื่อสินค้า
B = [] #ราคา
C = [] #จำนวน
total = 0
print(f"โปรแกรมคำนวณสินค้า")
print(f"กด q เพื่อสรุป")
while True:
    print(f"กรอกชื่อสินค้า (กรอก Q เพื่อสรุป ) : ")
    name = input()
    if name.lower() == 'q':
        break
    try:
         B1 = float(input(f"ราคา : "))
         C1 = float(input(f"จำนวนสินค้า : "))
    except ValueError:
        print(f"กรอกตัวเลข!!!!!")
        continue
    A.append(name) #เพิ่มค่าเข้าไปต่อแถวใน​ list
    B.append(B1)
    C.append(C1)
    print(A)
    print(B)
    print(C)