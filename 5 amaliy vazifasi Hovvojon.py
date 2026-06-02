#1 elektron pochta manzilini tekshirish
pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
for pochta in pochtalar:
    if "@"  not in pochta:
        print(f"Noto'g'ri email: {pochta}")



#2. Parol Kuchini Tekshirish:
# parollar= ["password123", "Qwerty!", "admin", "StrongPass1!"]
# maxsus_bel ="!@#$%^&*()_+=<>?/."
# for parol in parollar:
#     if len(parol)<8:
#         print("Juda qisqa")
#







#3 ob-havo
haroratlar =[20,22,19,24,25,23,21]
ortacha =sum(haroratlar)/len (haroratlar)
print("O'rtacha harorat", ortacha)
for h in haroratlar:
    if h >22:
        print(h, "Iliq kun")
    else:
        print(h, "Salqin kun")


#4 Restaran buyurtmalari
taomlar =["Osh","Manti","Shashlik","Lagmon"]
buyurtma =input("Taom kiriting:")
for taom in taomlar:
    if buyurtma in  taomlar:
        print("Buyutmangiz qabul qilindi")
    else:
        print("Kechirasiz, bunday taom yo'q")



#5 Anketa
yoshlar = [16, 21, 17, 30, 25]
for yosh in yoshlar:
    if yosh < 18:
        print(f"Yosh: {yosh} -> Yosh chegarasiga yetmagan")
    else:
        print(f"Yosh: {yosh} -> Xush kelibsiz")



#6Mobil ilova bildirishnomlarai
xabarlar = ["Yangi xabar", "Batareya past", "Yangilanish mavjud"]
for xabar in xabarlar:
    if xabar == "Batareya past":
        print("Telefoningizni quvvatlang")










