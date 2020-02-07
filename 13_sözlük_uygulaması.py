sozluk = dict()

while True:
    urun_ismi = input("Ürün ismini giriniz = ")
    if(urun_ismi == 'q'):
        break
    urun_adedi = input("Ürün adedi giriniz = ")
    sozluk[urun_ismi] = urun_adedi

print(sozluk)