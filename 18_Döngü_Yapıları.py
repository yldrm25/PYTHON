a = "b" in "a,b,c,d,e"
print(a)

b = "b" in "a,c,d,r,f,g"
print(b)

c = 5 in [1,2,3,4,5,6,7,8,9,0]
print(c)

d = 10 in [1,2,3,4,5,6,7,8,9,0]
print(d)

print("---------------------------------------------")
print("")
# for döngüsü çalışamaları

liste = [1,2,3,4,5]

for a in liste:
    print(a)

print(type(liste))

print("---------")

demet = (1,2,3,4,5,6)

for a in demet:
    print(a)
print(type(demet))

print("--------------")

liste2 = [1,2,3,4,5]

toplam = 0

for a in liste2:
    toplam += a
print(toplam)

liste3 = [1,2,3,4,5,6,7,8,9]

topla = 0

for a in liste3:
    topla += a
print(topla)

print("-----------------------")
# listedeli tek sayıları bulan program
print("--- Listedeki 1'den 10'a kadar olan sayıdan tek olanları bulan yazılım ---")
liste4 = [1,2,3,4,5,6,7,8,9,10]

for a in liste4:
    if (a % 2 != 0):
        print(a)

print("---------")
print("--- Listedeki 1'den 20'ye kadar olan sayılardan çift olanları bulmak ---")
liste5 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for a in liste5:
    if (a %2 == 0):
        print(a)

print("--------------")
# Liste içerisindeki tuple yani demet içerisindeki verilere ulaşmak...

liste6 = [1,2,3,4,5,6,7,8,9,10]

for c in liste6:
    if (c>5):
        print(c)






















