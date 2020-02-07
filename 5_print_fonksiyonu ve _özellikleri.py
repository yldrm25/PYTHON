# "\n" bir kere ters slash ve n harfi koyarsanız alt satıra geçer.
print("İSMAİL \n\nBUSE ")

# "\t" ters slash t harfi ise tab tuşuna basılmış gibi boşluk bırakır.
print("İSMAİL \t \t BUSE")

a = "ismail"
b = "yıldırım"
c = "buse"
d = "yıldırım"

# sep="" bu fonksiyon print ile kullanılır .
# sep fonksiyonu yazılacak olan değerlerin aralarına gelecek karakteri topluca ayarlamak için kullanılır.
print(a,b,c,d)
print("ismail","yıldırım",25,30,42)

print("")
print(*"TBMM",sep=".")