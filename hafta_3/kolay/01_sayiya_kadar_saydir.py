"""
Kullanıcıdan Sayıya Kadar Toplam:

Kullanıcıdan bir tamsayı iste (örn: 10).

1'den bu sayıya kadar olan (sayı dahil) tüm sayıları toplayan ve sonucu ekrana yazdıran bir for döngüsü yaz.

Matematiksel formül kullanma, döngüyle topla.
"""


sayi = int(input("Kaça Kadar Saymak İstiyorsunuz : "))

x = 0

for i  in range(sayi+1):
    x = i + x

print(x)