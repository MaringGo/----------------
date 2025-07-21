#โปรเเกรมคำนวณค่า BMI (ดรรชีมวลกาย)
m = float(input("กรอกค่าน้ำหนัก(กก.) : "))
n = float(input("กรอกส่วนสูง(ม.) : "))
mi = m/(n*n)
print(f"น้ำหนัก {m} กก.")
print(f"ส่วนสูง {n} ม.")
print(f"BMI = {mi:.2f}")
if (mi >= 30) :
    print (f"อ้วนระดับที่ 2")
elif (mi >= 25) :
    print (f"อ้วนระดับที่ 1")
elif (mi >= 23) :
    print (f"เกินมาตรฐาน") 
elif (mi >= 18.5) :
    print (f"มาตรฐาน")       
elif (mi <= 18.5) :
    print (f"ต่ำกว่าเกณฑ์")