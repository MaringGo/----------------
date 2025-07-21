#คำสั่งวนลูป for , while
#แสดงเลขคี่ตั้งแต่ 1-20 บนจอ
print (f"กรอกจำนวนเริ่มต้น : ")
x = int(input())
print (f"กรอกจำนวนสุดท้าย : ")
y = int(input())
print (f"กรอกเลข 0 เลขคู่ หรือ กรอกเลข 1 เลขคี่")
z = int(input())
for i in range(x, y):
     if ( i % 2 == z ):
       print(i)