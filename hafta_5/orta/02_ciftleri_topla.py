"""
Sadece Çiftleri Topla:

ciftleri_topla adında bir fonksiyon yaz.

Parametre olarak bir sayı listesi alsın (örn: [1, 2, 3, 4, 6]).

Fonksiyon listenin içindeki sadece çift sayıları bulup toplasın ve toplam sonucunu döndürsün.

Kendi oluşturduğun bir liste ile test et.
"""

def ciftleri_topla(sayilar):
    
    topla = 0

    for i in sayilar:
        if i % 2 == 0:
            topla += i
    return topla


liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print("Çift Sayılar : ",ciftleri_topla(liste))

