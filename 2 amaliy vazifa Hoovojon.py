#capitalize()	Converts the first character to upper case- birinchi harfni katta qiladi
ism ="hovvojon"
print(ism.capitalize())
viloyat ="xorazm"
print(viloyat.capitalize())

#casefold()	Converts string into lower case
matn2 ="groß"
print(matn2.casefold)
matn1 ="NAME"
print(matn1.casefold())

#center()	Returns a centered string
print("python".center(10,"*"))
print("dunyo".center(30,"*"))

#count()	Returns the number of times a specified value occurs in a string
matn ="olma, o'rik, shaftoli, olma , anjir"
print(matn.count("olma"))
mashina ="damas, nexia, cobalt, damas, spark, damas"
print(mashina.count("damas"))

#encode()	Returns an encoded version of the string
matin ="Salom"
almashtirish =matin.encode("utf-8")
print(almashtirish)
nom ="Toshkent"
ozgarish =nom.encode("utf-8")

#endswith()	Returns true if the string ends with the specified value
matn ="Men o'qishda o'qiyman"
print(matn.endswith("o'qiyman"))
matn1 ="Men kitob o'qishni yaxshi ko'raman"
print(matn1.endswith("o'qishni yaxshi"))

#expandtabs()	Sets the tab size of the string
matn ="Men\tsen\tbiz"
print(matin.expandtabs(7))
matn1 ="Salom\tdunyo\thayot"
print(matin.expandtabs(7))

#find()	Searches the string for a specified value and returns the position of where it was found
matin ="Men python kursiga boraman"
print(matin.find("python"))
matin1 ="Men 2 kurs talabasiman"
print(matin.find("kurs"))

#format()	Formats specified values in a string
ism ="Hovvojon"
print("Mening ismim {}".format(ism))
familiya ="Rustamova"
print("Mening familiyam {}.".format(familiya))\

#format_map()	Formats specified values in a string
matn7 = "Talaba {ism} {yosh} yoshda. Yo'nalishi: {yunalish}."
talaba = {"ism": "Hovvojon", "yosh": 20, "yunalish": "Axborot xavfsizligi"}
print(matn7)
matn3 = "Talaba {ism} {yosh} yoshda. Yo'nalishi: {yunalish}."
talaba1 = {"ism": "Maftuna", "yosh": 27, "yunalish": "Axborot xavfsizligi"}
print(matn3)

#index()	Searches the string for a specified value and returns the position of where it was found
matin ="Men talabaman"
print(matin.index("talabaman"))
ism ="Rustamova Hovvojon"
print(ism.index("Rustamova"))

#isalnum()	Returns True if all characters in the string are alphanumeric
matin ="Men12"
print(matin.isalnum())
matin2 ="Salom dunyo"
print(matin2.isalnum())

#isalpha()	Returns True if all characters in the string are in the alphabet
matin ="ona"
print(matin.isalpha())
matin ="aka2"
print(matin.isalpha())

#isascii()	Returns True if all characters in the string are ascii characters
matin ="Hello world"
print(matin.isascii())
matin12="прллоо"
print(matin12.isascii())

#isdecimal()	Returns True if all characters in the string are decimals
kod ="1234"
print(kod.isdecimal())
kod1 ="12a34"
print(kod1.isdecimal())

#isdigit()	Returns True if all characters in the string are digits
kod ="1234"
print(kod.isdigit())
kod1 ="5²"
print(kod1.isdigit())

#isidentifier()	Returns True if the string is an identifier
nom ="variable"
print(nom.isidentifier())
nom1 ="ism"
print(nom1.isidentifier())

#islower()	Returns True if all characters in the string are lower case
matin ="dasturchi"
print(matin.islower())
matin7 ="Dasturchi"
print(matin7.islower())

#isnumeric()	Returns True if all characters in the string are numeric
kod1 ="100"
print(kod.isnumeric())
kod3 ="100 dollor"
print(kod.isnumeric())

#isprintable()	Returns True if all characters in the string are printable
matin19 ="Salom dunyo 213"
print(matin19.isprintable())
matin14 ="Salom\ndunyo"
print(matin14.isprintable())

#isspace()	Returns True if all characters in the string are whitespaces
matin =" "
print(matin.isspace())
matin45 ="\t\n"
print(matin45.isspace())

#istitle()	Returns True if the string follows the rules of a title
matin ="Salom Dasturlash tili"
print(matin.istitle())
matin23 ="Salom Dssturlash Tili"
print(matin23.istitle())

#isupper()	Returns True if all characters in the string are upper case
matn10 = "PYTHON"
print(matn1.isupper())
matn3 = "PYTHONp"
print(matn3.isupper())