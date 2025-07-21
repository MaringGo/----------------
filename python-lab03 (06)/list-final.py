nickname = []
total = 0
#ให้กรอกชื่อเล่นไปเรื่อยๆเมื่อพอใจแล้วให้พิมพ์ X
#เมื่อกด X ให้สรุปจำนวนเพื่อนทั้งหมด
#จากนั้นแสดงรายชื่อเพื่อน โดยเรียงจาก A-Z
#sorted() เรียงข้อมูลใน list
while True:
    print(f"กรอกชื่อเพื่อน(ENG)((พิมพ์ x เพื่อสรุป)) : ")
    name = input()
    if name.lower() == 'x':
        break
    nickname.append(name)
    print(nickname)
print(f"เพื่อนทั้งหมด {len(nickname)} คน")
print(f"รายชื่อเพื่อน A-Z")
sorted_nickname = sorted(nickname)
for i in range(len(nickname)):
    print(sorted_nickname[i])