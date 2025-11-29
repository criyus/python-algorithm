"""
Asal Sayı Kontrolü (Hacker'ların Vazgeçilmezi):

asal_mi adında bir fonksiyon yaz.

Bir sayı alsın. Sayı Asal ise True, değilse False döndürsün.

Mantık: Sayı, 2'den başlayıp kendisine kadar (kendisi hariç) hiçbir sayıya tam bölünmemeli.

Test: 1'den 50'ye kadar olan sayıları bir döngüye sok ve bu fonksiyonu kullanarak sadece asal olanları ekrana yazdır.
"""

def asal_mi(sayi):
    if sayi < 2:
        return False 
        
    for i in range(2, sayi):
        if sayi % i == 0:
            return False 
    
    return True 

x = int(input("Sayı Giriniz: "))

print("Asal mı ? ",asal_mi(x))
