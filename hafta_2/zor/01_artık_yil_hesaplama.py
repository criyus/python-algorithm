"""
Artık Yıl (Leap Year) Hesaplayıcı: Bir yılın "Artık Yıl" (şubatın 29 çektiği yıl) olup olmadığını bulan bir program yaz. Kurallar şöyledir:

Yıl 4'e tam bölünmelidir.

ANCAK; eğer yıl 100'e tam bölünüyorsa, 400'e de tam bölünmelidir.

Örnek: 2000 (Artık Yıl), 1900 (Artık Yıl Değil), 2024 (Artık Yıl).

Kullanıcıdan yılı iste ve durumu yazdır.
"""

yil = int(input("Yıl giriniz: "))


if (yil % 4 == 0) and (yil % 100 != 0 or yil % 400 == 0):
    print(yil,"Artık Yıldır.")
else:
    print(yil,"Artık Yıl Değildir.")