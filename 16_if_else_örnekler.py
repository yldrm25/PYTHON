# Vizenin yüzde 40 finalin yüzde 60 ını alan ve harf notu veren program...

print("vize final notu hesaplama")
print("")
vize = int(input("Vize notu giriniz : "))
final = int(input("Final Notu girini : "))

ortalama = (vize/100)*40 + (final/100)*60

if (ortalama > 80 and ortalama <= 100):
    print("--------------------------")
    print("ORTALAMA => {}".format(ortalama))
    print("Harf notu => AA")
    print("--------------------------")

elif (ortalama > 70 and ortalama <= 80):
    print("--------------------------")
    print("ORTALAMA => {}".format(ortalama))
    print("Harf Notu => BA")
    print("--------------------------")

elif (ortalama > 50 and ortalama <= 70):
    print("--------------------------")
    print("ORTALAMA => {}".format(ortalama))
    print("Harf Notu => CB")
    print("--------------------------")

elif (ortalama > 40 and ortalama <= 50):
    print("--------------------------")
    print("ORTALAMA => {}".format(ortalama))
    print("Harf notu => DC")
    print("--------------------------")

elif (ortalama > 30 and ortalama <= 40):
    print("--------------------------")
    print("ORTALAMA => {}".format(ortalama))
    print("Harf notu => ED")
    print("--------------------------")

elif (ortalama > 0 and ortalama <=30):
    print("--------------------------")
    print("ORTALAMA => {}".format(ortalama))
    print("Harf Notu => FF    KALDOIN")
    print("--------------------------")


