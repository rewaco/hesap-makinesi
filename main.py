print("lütfen yapılacak işlemi seçiniz")
print(" 1:Toplama \n 2:Cıkarma \n 3:Çarpma \n 4:Bölme")

carpma = "*"
toplama = "+"
cıkarma = "-"
bölme ="//"

secim = input("")

sayı1 = input("lütfen ilk sayıyı giriniz")

sayı2 = input("lütfen ikinci sayıyı giriniz")

sayı2 = int(sayı2)
sayı1 = int(sayı1)
secim = int(secim)


if secim == 1:
    print(sayı1,toplama,sayı2)
    print(sayı1 + sayı2)
elif secim == 2:
    print(sayı1,cıkarma,sayı2)
    print(sayı1 - sayı2)
elif secim == 3:
    print(sayı1,carpma,sayı2)
    print(sayı1 * sayı2)
elif secim == 4:
    print(sayı1,bölme,sayı2)
    print(sayı1 // sayı2)
else:
    print("Hata")


