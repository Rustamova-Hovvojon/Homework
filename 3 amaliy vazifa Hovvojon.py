#append
sonlar2 = [1,4,7,10]
sonlar2.append(13)
print(sonlar2)
mevalar =[ 'olma', 'gilos','shaftoli']
mevalar.append('uzum')
print(mevalar)

#clear
sonlar =[ 2,5,6,8]
sonlar.clear()
print(sonlar)
matinlar =["olma", "uzum", "banan"]
matinlar.clear()
print(matinlar)

#copy
a= [1,3,5,7,8]
b =a.copy()
print(b)
matin2 =["salom", "dunyo"]
nusxa =matin2.copy()
print(nusxa)

#count
a =[2,4,6,7,5,6,5,7,5]
print(a.count(5))
mevalar =['olma', 'gilos', 'olma', 'banan']
print(mevalar.count('olma'))

#extend
a =[1,2,3]
b =[4,5,6]
a.extend(b)
print(a)
mashina =['damas', 'lacetti']
mashina2 =['cobalt']
mashina2.extend(mashina)
print(mashina2)

#index
mevalar = ["olma", "banan", "uzum"]
print(mevalar.index("banan"))
sonlar = [10, 20, 30, 40]
print(sonlar.index(30))

#insert
sonlar = [1, 2, 4]
sonlar.insert(2,3)
print(sonlar)

mevalar = ["olma", "uzum"]
mevalar.insert(1, "banan")
print(mevalar)


#pop
sonlar = [10, 20, 30]
sonlar.pop()
print(sonlar)

harflar = ["a", "b", "c"]
harflar.pop(1)
print(harflar)

#remove
sonlar = [1, 2, 3, 2]
sonlar.remove(2)

print(sonlar)
mevalar = ["olma", "banan", "uzum"]
mevalar.remove("banan")

#reverse
print(mevalar)
sonlar = [1, 2, 3, 4]
sonlar.reverse()
print(sonlar)

harflar = ["a", "b", "c"]
harflar.reverse()
print(harflar)

#sort
sonlar = [5, 2, 8, 1]
sonlar.sort()
print(sonlar)

mevalar = ["uzum", "olma", "banan"]
mevalar.sort()
print(mevalar)

