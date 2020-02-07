a = 15
b = 10

if (a>b):
    print("{} > {}".format(a,b))

print("a büyükse b den yukarıda yazdırılacak .")


print("----------------")


sayı1 = int(input("Sayı 1 giriniz : "))
sayı2 = int(input("Sayı 2 giriniz : "))

if (sayı1>sayı2):
    print("")
    print("{} büyüktür {} den".format(sayı1,sayı2))

elif (sayı1 == sayı2):
    print("")
    print("iki sayıda eşittir")

elif (sayı1 < sayı2):
    print("")
    print("{} büyüktür {} den".format(sayı2,sayı1))

print("----------------------------------------------------")
print("Girilen sayının tek mi çift mi olduğunu bulma")

sayigirin = int(input("Lüften bi sayı giriniz : "))

if sayigirin %2 == 0:
    print("")
    print("{} çifttir".format(sayigirin))
else:
    print("")
    print("{} tek sayıdır".format(sayigirin))

