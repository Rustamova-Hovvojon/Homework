
def istalgan_son(*sonlar):
    boshlangich_son=1
    for son in sonlar:
        boshlangich_son=boshlangich_son*son
    return boshlangich_son
print(istalgan_son(2,3,5,7,8))



#
def talaba_malumot(ism, familiya, **malumotlar):
    malumotlar['ism']=ism
    malumotlar['familiya']=familiya
    return malumotlar
talabalar=talaba_malumot('ism', 'familiya', yosh=20, t_yil=2006)
print(talabalar)


#
def ortacha_baho(ism, *baholar):
    ortacha=sum(baholar)/len(baholar)
    return (f"{ism}ning o'rtacha bahosi: {ortacha}")
print(ortacha_baho("Hovvojon",5,4,5,5,4 ))


#
def malumot_yaratish(nom,**kwargs):
    mahsulot={"nom": nom}
    mahsulot.update(kwargs)
    return mahsulot
print(malumot_yaratish("Iphone 16", narx=1200, rang="oq", brend="Apple", xotira="256 GB"))

