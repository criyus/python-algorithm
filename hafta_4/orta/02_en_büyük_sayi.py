"""
En Büyük Sayıyı Bul (Hacker Usulü - max() YASAK!):

notlar = [67, 89, 45, 92, 34, 76, 12, 98, 55]

Python'ın hazır max() fonksiyonunu kullanmadan, bir for döngüsü ve if yapısı kurarak bu listedeki en büyük sayıyı bulup ekrana yazdır.

İpucu: en_buyuk = 0 diye bir değişken tanımlayıp döngüdeki sayılarla kıyasla.
"""

notlar = [67, 89, 45, 92, 34, 76, 12, 98, 55]

en_büyük = notlar[0]

for i in notlar:

    if i >= en_büyük:
        en_büyük = i


print(en_büyük)