# Kullanıcı adı ve şifre sistemi

kadi = input("Kullanıcı adı giriniz : ")
sifre = input("Sifre giriniz : ")

if kadi == "ismail" and sifre == "yıldırım":
    print("giriş başarılı")
else:
    print("hatalı giriş")

print("------- ÖRNEKLER --------")
print("-----------------------------------------")

a = 5>9
print(a)

print("------------------------------------------")

b = 5>=4

print(b)

print("-------------------------------------------")

c = 5>=4 and "ismail" == "ismail"

print(c)

print("--------------------------------------------")

d = 3 < 9 or "ismail" == "buse" or "yıldırım" == "ceviz"

print(d)

print("----------------------------------------------")

e = "ismail" == "buse" or 5>9

print(e)