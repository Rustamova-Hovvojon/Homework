while True:
    rang = input("Svetafor rangini kiriting: ").lower()

    if rang == "qizil" or rang == "sariq" or rang == "yashil":
        print("Rahmat, to'g'ri rang kiritildi")
        break
    else:
        print("Xato rang, qayta kiriting")







#2
import random
tasodifiy_son = random.randint(1, 10)
while True:
    son = int(input("1 dan 10 gacha son kiriting: "))
    if son == tasodifiy_son:
        print("Tabriklaymiz, siz topdingiz!")
        break
    else:
        print("Noto'g'ri, qayta urinib ko'ring")



#3
dostlar = []
while True:
    ism = input("Do'st ismini kiriting (to'xtatish uchun stop): ")
    if ism.lower() == "stop":
        break
    dostlar.append(ism)
print("Do'stlar ro'yxati:")
print(dostlar)



#4
kurs = 12600
while True:
    qiymat = input("USD summasini kiriting (chiqish uchun exit): ")
    if qiymat.lower() == "exit":
        print("Dastur tugadi")
        break
usd = float(qiymat)
som = usd * kurs
print("Natija:", som, "so'm")