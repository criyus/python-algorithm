"""
Dört İşlem Fonksiyonu:

hesapla adında bir fonksiyon yaz.

3 parametre alsın: sayi1, sayi2, islem.

islem parametresi string olarak "+", "-", "*", "/" alacak.

Fonksiyon gelen işleme göre sonucu hesaplayıp return etsin.

Kullanıcıdan sayıları ve işlemi alıp sonucu ekrana yazdır.
"""


def hesapla(say1,say2,islem):

    if islem == "+":
        return say1 + say2
    elif islem == "-":
        return say1 - say2
    elif islem == "*":
        return say1 * say2
    elif islem == "/":
        return say1 / say2
    else:
        print("Hatalı Giriş!")


say1 = int(input("1. Sayı : "))
say2 = int(input("2. Sayı : "))
islem = input("Yapılacak İşlem '+','-','*','/' :")

print("-----İşlemin Sonucu-----")
print(hesapla(say1,say2,islem))