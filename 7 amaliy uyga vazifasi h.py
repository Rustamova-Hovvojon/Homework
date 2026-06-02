# #################
def user_data(first_name, last_name, age):
    print("Ism:", first_name)
    print("Familiya:", last_name)
    print("Yosh:", age)

ism = input("Ismingizni kiriting: ")
familiya = input("Familiyangizni kiriting: ")
yosh = int(input("Yoshingizni kiriting: "))

user_data(ism, familiya, yosh)

# ##################
def find_max(a,b,c):
    max_son = max(a, b, c)

    if a == b == c:
        print(f"Eng katta son - A va B va C = {max_son}")
    elif a == b and a > c:
        print(f"Eng katta son - A va B = {max_son}")
    elif a == c and a > b:
        print(f"Eng katta son - A va C = {max_son}")
    elif b == c and b > a:
        print(f"Eng katta son - B va C = {max_son}")
    elif a == max_son:
        print(f"Eng katta son - A = {max_son}")
    elif b == max_son:
        print(f"Eng katta son - B = {max_son}")
    else:
        print(f"Eng katta son - C = {max_son}")

a = int(input("A sonini kiriting: "))
b = int(input("B sonini kiriting: "))
c = int(input("C sonini kiriting: "))

find_max(a, b, c)

########################
def find_letter_count(word, letter):
    count = word.count(letter)
    print(f'"{word}" sozida "{letter}" dan {count} ta.')
word = input("Soʻzni kiriting: ")
letter = input("Harfni kiriting: ")

find_letter_count(word, letter)

###########################
def list_sum(myList):
    print("Listning elementlar yig'indisi =", sum(myList))
myList = [5, 7, 20, 10]
list_sum(myList)

######################################################################################################
def daraja(a, b):
    print(a ** b)
a = int(input())
b = int(input())

daraja(a, b)

#############################
def daraja4(a, b, c, d):
    print(a ** b)
    print(a ** c)
    print(a ** d)

daraja4(2, 3, 4, 5)
#############################
def digit_count_and_sum(word):
    count = 0
    total = 0
    for i in word:
        if i.isdigit():
            count += 1
            total += int(i)

    print("Raqamlar soni =", count)
    print("Raqamlar yig'indisi =", total)

digit_count_and_sum("ab3c5d7")

##################################
def add_right(a, b):
    print(str(a) + str(b))

add_right(25, 8)

###################################
def add_left(a, b):
    print(str(b) + str(a))

add_left(25, 7)

##################################
def work_with_list(a):
    min_son = min(a)
    for i in range(len(a)):
        a[i] *= min_son
    print(a)

work_with_list([4, 2, 6, 8])

###################################
def big_sales(sales):
    return max(sales, key=sales.get)
sales = {
    "yanvar": 12000,
    "mart": 6000,
    "aprel": 15000,
    "sentabr": 9000,
    "dekabr": 10000
}

print(big_sales(sales))

#####################################
def min_max(numbers, max_num, min_num):
    if max_num == max(numbers):
        print(max_num, "eng katta son")
    else:
        print(max_num, "eng katta son emas")

    if min_num == min(numbers):
        print(min_num, "eng kichik son")
    else:
        print(min_num, "eng kichik son emas")

numbers = [3, 8, 18, 10, 5]

min_max(numbers, 18, 3)


#########################################
def expensiveProduct(products):
    eng_qimmat = max(products, key=lambda x: x["price"])
    print(eng_qimmat["name"])

products = [
    {
        "name": "Iphone X",
        "price": 600
    },
    {
        "name": "Iphone 12",
        "price": 1500
    },
    {
        "name": "Samsung Note 9",
        "price": 800
    },
    {
        "name": "Samsung S10",
        "price": 1100
    }
]

expensiveProduct(products)