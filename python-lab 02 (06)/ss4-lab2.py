print("=== โปรแกรมขายของอย่างง่าย ===")
product1 = input("กรอกชื่อสินค้า 1 : ")
price1 = float(input("กรอกราคาสินค้า 1 : "))
qty1 = int(input("กรอกจำนวนสินค้า 1 : "))
product2 = input("กรอกชื่อสินค้า 2 : ")
price2 = float(input("กรอกราคาสินค้า 2 : "))
qty2 = int(input("กรอกจำนวนสินค้า 2 : "))
product3 = input("กรอกชื่อสินค้า 3 : ")
price3 = float(input("กรอกราคาสินค้า 3 : "))
qty3 = int(input("กรอกจำนวนสินค้า 3 : "))
money = float(input("กรอกจำนวนเงินลูกค้า : "))
total1 = price1  * qty1
total2 = price2  * qty2
total3 = price3  * qty3
VAT = ((total1 + total2 + total3 ) * 7/107)
gramd_total = (total1 + total2 + total3) + VAT
gramd_total1 = (money - gramd_total)
print("\n== สรุปยอด ===")
print(f"{product1} x {qty1} = {total1:.2f} บาท")
print(f"{product2} x {qty2} = {total2:.2f} บาท")
print(f"{product3} x {qty3} = {total3:.2f} บาท")
print(f"ภาษี = {VAT:.2f}")
print(f"รวมทั้งหมด = {gramd_total:.2f} บาท")
print(f"เงินทอน = {gramd_total1:.2f} บาท")