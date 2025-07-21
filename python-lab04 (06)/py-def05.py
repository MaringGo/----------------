#โปกรแกรมตัดเกรด A B C D F
def cutgrade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

#รับคะแนนจากผู้ใช้
score = float(input("กรุณาใส่คะแนน: "))
grade = cutgrade(score)
print(f"เกรดของคุณคือ: {grade}")