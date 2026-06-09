# #soz uzunliki
# ismlar=['hovvojon', 'komila', 'maftuna', 'feruza', 'malak']
# uzunlik =list(map(len,ismlar))
# print(uzunlik)
#
#
# #Sonlarni satrga o'tkazish (map)
# sonlar =[1,2,5,6,8,9]
# matn =list(map(str,sonlar))
# print(matn)
#
# #Unli harf bilan boshlanuvchi so'zlarni topish (filter)
# sozlar = ["olma", "anor", "behi", "uzum", "shaftoli", "erik", "limon"]
# unlilar = "aeiouo‘"
# saralangan_sozlar = list(filter(lambda soz: soz[0].lower() in unlilar, sozlar))
# print(saralangan_sozlar)

# 3 xonali sonlarni ajratish (filter)
sonlar=[123, 2, 345, 20, 300, 2008, 478 ]
uch_xonali = list(filter(lambda x: 100 <= x <= 999, sonlar))
print("3 xonali sonlar:", uch_xonali)




#Ismlarga "Mr." qo'shish (map)
ismlar = ["Ali", "Vali", "Olim"]
janob_ismlar = list(map(lambda ism: f"Mr. {ism}", ismlar))
print("Yangi ismlar:", janob_ismlar)


#Juftlarini olib, 10 ga ko'paytirish (filter + map)
sonlar_2 = [1, 2, 3, 4, 5, 6]
juft_va_kopaytirilgan = list(map(lambda x: x * 10, filter(lambda x: x % 2 == 0, sonlar_2)))
print("Natija:", juft_va_kopaytirilgan)

