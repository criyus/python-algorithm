"""
Alan Hesaplayıcı (Varsayılan Değerli):

dikdortgen_alani adında bir fonksiyon yaz.

İki parametre alsın: kisa_kenar, uzun_kenar.

uzun_kenar için varsayılan değer 10 olsun.

Fonksiyon alanı hesaplayıp döndürsün.

Hem tek parametre (sadece kısa kenar) girerek hem de iki parametre girerek fonksiyonu test et.
"""

def dikdortgen_alani(kisa_kenar,uzun_kenar=10):
    alan = kisa_kenar * uzun_kenar
    return alan

kısa = int(input("Kısa Kenarını Giriniz : "))

uzun = int(input("Uzun Kenarı Giriniz : "))

x = dikdortgen_alani(kısa,uzun)

y = dikdortgen_alani(kısa)


print("Dikdörtgenin Alanı : ",x)

print("Uzun Kenar = 10 : ",y)
