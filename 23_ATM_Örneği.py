import time as zaman

print("AKBANK KANK'A HOŞGELDİNİ! İŞLEM YAPMAK İÇİN KARTINIZI SOKUNUZ : ")
secim = input("Katı sokmak için s, Bankadan ayrılmak için L yazınız : ")
mevcutpara = 1000

if (secim == "s"):
    print("Kartınız Okunuyor",end = "")
    for i in range(3):
        print(".",end="")
        zaman.sleep(1)
    while True:
        secenek = int(input("""
        *****************************
        1-KARTA PARA YÜKLE
        2-KARTTAN PARA ÇEK
        3-HESAP ÖZETİ
        4-ÇIKIŞ
        *****************************
        ===> """))

        while secenek < 1 or secenek > 4:
            secenek = int(input("Lütfen Belirtilen değerler içerisinde değer giriniz: "))


        if secenek == 1:
            print("--- HESABA PARA EKLEME ---")
            miktar = int(input("Miktar giriniz : "))
            mevcutpara = mevcutpara + miktar
        elif secenek == 2:
            print("--- HESAPTAN PARA ÇEKMEK ---")
            miktar = int(input("Miktar Giriniz : "))
            mevcutpara = mevcutpara - miktar
            print(mevcutpara)
        elif secenek == 3:
            print("--- HESAP ÖZETİ ---")
            print("""
            İsim = İsmail 
            Soyİsim = Yıldırım
            IBAN = XXXXXXXXXXXXXX
            Bakiye = {}
            
            """.format(mevcutpara))
        elif secenek == 4:
            print("İYİ GÜNLER DİLERİZ....")
            break





