a = 0
# while döngüsünde parantez içerisindeki koşul doğru ise döngü çalışır..
while(a < 21):
    if (a %2 == 0):
        print(a)
    a+=1

print("------------------------------------------")
# ismi girip ve kaç defa ismi yazdıracağını soran ve while döngüsüyle çalışan program....
isimAl = input("İsminizi Giriniz: ")
kacDefa = int(input("Kaç defa yazılsın = "))

while(kacDefa >0):
    print(isimAl)
    kacDefa-=1

print("")
print("sayac değişkenimize 5 değeri girdiğimiz için 5 adet isim yazdırıyor...")
isim = input("İsim giriniz : ")
sayac = 5

while(sayac>0):
    print(isim)
    sayac-=1

print("-----------------------------")
print("Listedeki sayları yazdırmak için index değişkeni yapıp birer birer yazdırdık..")

listesayilar = [1,2,3,4,5,6,7,8,9,10]
index = 0

while(len(listesayilar)> index):
    print(listesayilar[index])
    index+=1

print("-----------------")
print("Girilen sayıya kadar olan sayılar ardışık sayıyla yazdıran yazılım...")
sayac = 0
toplam = 0
sayi = int(input("Sayı giriniz : "))

while(sayi >= sayac):
    toplam = toplam+sayac
    print(toplam)
    sayac+=1

