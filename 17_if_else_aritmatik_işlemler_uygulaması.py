print("----- Aritmatik işlemler yapan uygulama -----")
islemler = int(input("1-Toplama\n2-Çıkarma\n3-Çarpma\n4-Bölme\n5-Çıkış\n\n==> "))


if islemler != 5:
    sayi1 = int(input("Sayı bir giriniz : "))
    sayi2 = int(input("Sayı iki giriniz : "))

if (islemler == 1):
    toplam = sayi1+sayi2
    print("{} + {} = {}".format(sayi1,sayi2,toplam))

elif (islemler == 2):
    cıkarma = sayi1 - sayi2
    print("{} - {} = {}".format(sayi1,sayi2,cıkarma))

elif (islemler == 3):
    carpma = sayi1*sayi2
    print("{} x {} = {}".format(sayi1,sayi2,carpma))

elif (islemler == 4):
    bolme = sayi1 / sayi2
    print("{} / {} = {}".format(sayi1,sayi2,bolme))

else:
    pass
    print("Çıkış yapılıyor ....")
