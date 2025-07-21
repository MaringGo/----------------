A = ["cola","pepsi","fanta"] #สินค้า
B = [10,15,20] #ราคา
C = [2,1,2] #จำนวน
total = 0
for i in range(len(A)):
    #cola x 10 2 = 20 บาท
    sum = B[i]*C[i]
    total = total + sum
    print(f" {A[i]} x {B[i]} x {C[i]} = {B[i]*C[i]} บาท")
print(f"ยอดรวมคือ {total}")