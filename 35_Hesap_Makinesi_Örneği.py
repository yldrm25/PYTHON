print("HESAP MAKİNESİNE HOŞ GELDİNİZ")

sayi1 = 0
sayi2 = 0

while True:

    islem = int(input("""
                      ARİTMATİK İŞLEMLER YAPMAK İÇİN BİR İŞLEM SEÇİN ?

                       1-toplama               
                       2-çıkarma
                       3-çarpma
                       4-bölme
                       5-çıkış

                     ===> """))
    while islem < 1 or islem > 5:
        islem = int(input("Lütfen işlem değerlerine göre giriniz : "))

    if islem == 1:
        print("------------------")
        print("TOPLAMA İŞLEMİ")
        sayi1 = int(input("Sayı bir giriniz : "))
        sayi2 = int(input("Sayı iki giriniz : "))
        print("------------------")
        toplam = sayi1 + sayi2
        print("TOPLAM : ",toplam)
        print("------------------")
    elif islem == 2:
        print("------------------")
        print("ÇIKARMA İŞLEMİ")
        sayi1 = int(input("Sayı bir giriniz : "))
        sayi2 = int(input("Sayı iki giriniz : "))
        fark = sayi1 - sayi2
        print("------------------")
        print(fark)
        print("------------------")
    elif islem == 3:
        print("ÇARPMA İŞLEMİ")
        print("------------------")
        sayi1 = int(input("Sayı bir giriniz : "))
        sayi2 = int(input("Sayı iki giriniz : "))
        carpım = sayi1 * sayi2
        print("------------------")
        print(carpım)
        print("------------------")
    elif islem == 4:
        print("BÖLME İŞLEMİ")
        print("------------------")
        sayi1 = int(input("Sayı bir giriniz : "))
        sayi2 = int(input("Sayı iki giriniz : "))
        bolum = sayi1 / sayi2
        print("------------------")
        print(bolum)
        print("------------------")
    elif islem == 5:
        print("--- GÖRÜŞMEK ÜZERE ---")
        break

