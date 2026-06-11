class Web_sahifa:
    def __init__(self, ism, foydalanuvchi_ismi, tyil, jinsi,  email, profil_rasm, password, tel_nomer):
        self.ism=ism
        self.foydalanuvchi_ismi =foydalanuvchi_ismi
        self.tyil = tyil
        self.jinsi=jinsi
        self.email = email
        self.profil_rasm =profil_rasm
        self.password = password
        self.tel_nomer= tel_nomer

    def get_info(self):
         return (f"Foydalanuvchi: {self.foydalanuvchi_ismi}, "
                    f"Ismi: {self.ism}, "
                    f"Tug'ilgan yili: {self.tyil}, "
                    f"Jinsi: {self.jinsi}, "
                    f"Email: {self.email},"
                    f"profil_rasm:{self.profil_rasm} ,"
                    f"password:{self.password,}"
                    f"Telefon: {self.tel_nomer}")

# 3-misol: obyektlar yaratish
obyekt1 =Web_sahifa("Ali", "ali2004", 2004, "Erkak", "ali@gmail.com", "ali.jpg", "12345", "+998901112233")
obyekt2 = Web_sahifa( "Malika", "malika01", 2005, "Ayol", "malika@gmail.com", "malika.jpg", "54321", "+998909998877")
obyekt3 = Web_sahifa("Jasur", "jasur777", 2003, "Erkak", "jasur@gmail.com", "jasur.jpg", "77777", "+998935556677")

# Metodga murojaat qilish
print(obyekt1.get_info())
print(obyekt2.get_info())
print(obyekt3.get_info())

# Xususiyatlarga murojaat qilish
print(obyekt1.ism)
print(obyekt2.email)
print(obyekt3.tel_nomer)
