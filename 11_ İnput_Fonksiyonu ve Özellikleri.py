isim = input("isminizi giriniz :")

print(isim)

print("--------------------")

sayi = int(input("Sayı giriniz : "))

print("Girilen sayı 5 ile çarpıldı : ",sayi*5)

print("--------------------")

print("*** Toplama işlemi ***")
s1 = int(input("Sayı 1 giriniz : "))
s2 = int(input("Sayı 2 giriniz : "))

toplam = s1+s2

print("TOPLAM => ",toplam)

print("----------------------------")

film = []

film_ismi = input("Film ismi giriniz :")
film_imdb = float(input("IMDB puanı giriniz :"))
print("")
print("---------------")
film.append(film_ismi)
film.append(film_imdb)

print("Filim ismi : {}\n Film imdb : {}".format(film_ismi,film_imdb))
print("---------------")

print("---------------------------------------------")

