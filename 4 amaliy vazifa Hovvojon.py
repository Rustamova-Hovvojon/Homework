#ob
havo =int(input("Bugun havo harorati qanday?"))
if havo<= 0:
    print("Sovuq")
elif havo<=20:
    print("Salqin")
elif havo<=30:
    print("Iliq")
else:
    print("Issiq")




# Internet
summa =float(input("Xarid summasini kiriting? "))
if summa<=50000:
    print("Chegirma yo'q")
if summa<=100000:
    chegirma =summa * 0.05
    print("chegirma ", chegirma )
    #print("Yakuniy narx":, summa)
if summa>100000:
    print(f"10% chegirma{summa}")


 #Tizimga Kirish
login = input("Loginni kiriting: ")
parol = input("Parolni kiriting: ")
if login == "admin" and parol == "12345":
    print("Xush kelibsiz, admin!")
else:
    print("Login yoki parol xato")

#film45

yosh = int(input("Yoshingizni kiriting: "))
if yosh < 13:
     print("Sizga ushbu film tavsiya etilmaydi")
elif yosh <= 17:
    print("Siz filmni ota-onangiz bilan ko'rishingiz mumkin")
else:
    print("Siz filmni tomosha qilishingiz mumkin")


#Restoran Menyusi
print("1 - Osh")
print("2 - Mastava")
print("3 - Shashlik")
tanlov = int(input("Tanlovni kiriting: "))
if tanlov == 1:
    print("Osh - 25 000 so'm, 15 daqiqa")
elif tanlov == 2:
    print("Mastava - 20 000 so'm, 10 daqiqa")
elif tanlov == 3:
    print("Shashlik - 30 000 so'm, 20 daqiqa")
else:
    print("Noto'g'ri tanlov")

#Talaba Baholash Tizimi
ball = int(input("Ballni kiriting: "))
if 86 <= ball <= 100:
    print("5 baho")
elif 70 <= ball <= 85:
    print("4 baho")
elif 55 <= ball <= 69:
    print("3 baho")
else:
    print("2 baho")


#Bankomat Pul Yechish
karta = int(input("Kartadagi summani kiriting: "))
yechish = int(input("Yechiladigan summani kiriting: "))
if yechish < 5000:
    print("Minimal yechish summasi 5000 so'm")
elif karta < yechish:
    print("Hisobda yetarli mablag' mavjud emas")
else:
    print("Pul muvaffaqiyatli yechildi")
    print("Qolgan mablag':", karta - yechish)

#Ish Jadvalini Tekshirish
kun = input("Hafta kunini kiriting: ")
if kun == "Shanba" or kun == "Yakshanba":
    print("Bugun dam olish kuni")
else:
    print("Bugun ish kuni")

#mobil tarif
gb = float(input("Oyiga ishlatiladigan internetni kiriting (GB): "))
if gb < 1:
    print("Sizga 'Mini' tarifi mos keladi")
elif gb <= 5:
    print("Sizga 'Standart' tarifi mos keladi")
else:
    print("Sizga 'Unlimited' tarifi mos keladi")