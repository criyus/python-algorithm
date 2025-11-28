"""
Tek Sayıları Ayıklama:

Kullanıcıdan bir sayı girmesini iste (örn: 20).

1'den bu sayıya kadar olan sayılar içinde sadece TEK olanları ekrana yazdıran bir for döngüsü kur.
(% operatörünü hatırla).
"""

sayi = int(input("Kaça Kadar Tek Sayıları Yazdırmak İstersin : "))

for i in range(sayi):
    if i % 2 != 0 :
        print(i)
