"""
En Büyük Sayıyı Bulma (Hazır Fonksiyon Yok!):

Kullanıcıdan 3 farklı sayı girmesini iste (a, b, c).

max() fonksiyonunu kullanmadan, sadece if, elif ve mantıksal operatörler (and) kullanarak 
bu üç sayıdan en büyüğünü bulup ekrana yazdır.
"""

a = int(input("Birinci Sayı :"))
b = int(input("Birinci Sayı :"))
c = int(input("Birinci Sayı :"))

if a >= b and a >= c:
    print("Büyük Sayı:", a)
elif b >= a and b >= c:
    print("Büyük Sayı:", b)
else:
    print("Büyük Sayı:", c)