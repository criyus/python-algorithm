"""
Pozitif ve Negatif Ayırıcı:

Kullanıcıdan 10 tane sayı girmesini iste (pozitif veya negatif olabilir).

Bu sayıları kontrol et:

Pozitif ise pozitifler listesine ekle.

Negatif ise negatifler listesine ekle.

Program sonunda: "Pozitifler Listesi: [...]" ve "Negatifler Listesi: [...]" şeklinde yazdır.
"""

sayilar = []

pozitif = []

negatif = []

for i in range(1,11):
    sayilar.append(int(input(f'{i}. Sayıyı Giriniz : ')))

for i in sayilar:
    if i > 0 :
            pozitif.append(i)
    else:
            negatif.append(i)

print("Pozitif Listesi :",pozitif)
print("Negatif Listesi :",negatif)
