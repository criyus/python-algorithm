"""
Mükemmel Sayı Kontrolü (Algoritma):

Kullanıcıdan bir sayı al (örn: 6 veya 28).

Bu sayının kendisi hariç pozitif tam bölenlerini bul ve topla.

Eğer bölenlerin toplamı, sayının kendisine eşitse ekrana "Mükemmel Sayı", değilse "Mükemmel Sayı Değil" yazdır.

Örnek: 6 -> Bölenleri 1, 2, 3. Toplamı: 1+2+3 = 6 (Mükemmel).
"""

sayi = int(input("Bir Sayi Gir : "))

x = 0

for i in range(1,sayi):

    if sayi % i == 0:
        x = i + x
if x == sayi:
    print("Mükemmel Sayı")
else:
    print("Mükemmel Sayı Değil")