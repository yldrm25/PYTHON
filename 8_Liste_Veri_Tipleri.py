print("----------------------LİSTELER VERİ TİPLERİ ----------------------------------")

liste = [0,1,2,5,9,10,"BUSEM"]
print(liste)
print(type(liste))
print(len(liste))
print("---------------")


liste2 = [1,2,3,4,5,6,7,8,9,10]

print(liste2)

# Burada listenin birinci karakterini değiştirdik.
liste2 [0] = 10
print(liste2)

print("----------------")

isim = "Buse"

liste3 = list(isim)

print(liste3)

liste3 [0] = "İ"
print(liste3)
print(liste3[0:3])

yeni_liste = (liste3[0:3])
print(yeni_liste)

# Bu [::-1] şeklinde yazarsak tersten yazdırır.
print(liste3[::-1])

print("------------------------")

liste4 = [1,2,3,4,5]
liste5 = [6,7,8,9,10]

toplalist = liste4+liste5

toplalist = toplalist+ ["Busem"]

print(*(toplalist),sep=" -- ")

print("---------------------------")

# append listeye yeni bir eleman eklemeye yarıyor.
listem = [1,2,3,4,5]

listem.append(6)
listem.append(7)
listem.append(8)
listem.append(9)
listem.append(10)
listem.append("BUSE")
print(listem)

print("------------------------")

listepop = [0,1,2,3,"buse"]

listepop.pop(2)
print(listepop)

print(listepop[2])
print("------------------------")

listeshort = [1,5,20,90,3,50,70,60,40,250,800,80,65,38,95,75]

# Liste içerisindeki elemanları küçükten büyüğe sıralamak için sort fonksiyonu kullanılır.
listeshort.sort()
print(listeshort)
#sort fonksiyonun reverse=True yaparsak tersten yani büyükten küçüğe sıralar.
listeshort.sort(reverse=True)
print(listeshort)

print("----------------------------------")

# Liste içinde liste aşşağıdaki gibi yapılır..
listeiciliste = [1,2,3,4],[5,6,7],[8,9,10]

print(listeiciliste [0] [1])






















