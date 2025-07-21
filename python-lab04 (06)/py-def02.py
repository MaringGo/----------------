#ฟังก์ชันที่มีการคำนวณ
#2025 + 543 = 2568
#โปรแกรมแปลงปี ค.ศ. เป็น พ.ศ.
def convert_toBE(year):
    print(f"ปี ค.ศ {year} เป็นปี พ.ศ. = {year + 543}")
def convert_toCE(year):
    print(f"ปี พ.ศ {year} เป็นปี ค.ศ. = {year - 543}")
#เรียกใช้งานฟังก์ชัน
#ค.ศ เป็น พ.ศ
convert_toBE(int(input(f"กรอก ปี ค.ศ. ที่ต้องการแปลง: ")))
#พ.ศ เป็น ค.ศ
convert_toCE(int(input(f"กรอก ปี พ.ศ. ที่ต้องการแปลง: ")))