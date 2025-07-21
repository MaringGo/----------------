# โปรแกรม POS อย่างง่าย (ไม่ใช้ array)
print("=== โปรแกรมขายของอย่างง่าย ===")
# รับข้อมูลสินค้า
product1 = input("กรอกชื่อสินค้า 1 : ")
price1 = float(input("กรอกราคาสินค้า 1 : "))
qty1 = int(input("กรอกจำนวนสินค้า 1 : "))
product2 = input("กรอกชื่อสินค้า 2 : ")
price2 = float(input("กรอกราคาสินค้า 2 : "))
qty2 = int(input("กรอกจำนวนสินค้า 2 : "))
# คำนวณ
total1 = price1 * qty1
total2 = price2 * qty2
gramd_total = total1 + total2
# แสดงผล
print("\n== สรุปยอด ===")
print(f"{product1} x {qty1} = {total1:.2f} บาท")
print(f"{product2} x {qty2} = {total2:.2f} บาท")
print(f"รวมทั้งหมด = {gramd_total:.2f} บาท")