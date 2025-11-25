"""
Zaman Dönüştürücü (Klasik Algoritma): Elinizde toplam_saniye = 3750 diye bir değişken var. 
Sadece // (tam bölme) ve % (mod) operatörlerini kullanarak bu sürenin kaç Saat, kaç Dakika ve kaç Saniye ettiğini hesaplayıp ekrana şöyle yazdıran kodu yaz: "1 Saat 2 Dakika 30 Saniye" 
(İpucu: Önce saati bul, kalanı dakikaya çevir, en son kalanı saniye yap.)
"""

toplam_saniye = 3750

saat = toplam_saniye // 3600 # saati bulur
kalan = toplam_saniye % 3600 # saati bulunca kalan saniyeyi hesaplar

dakika = kalan // 60 # dakikayı bulur

saniye = kalan % 60 # dakikadan kalan sani




print(f'{saat}saat,{dakika}dakika,{saniye}saniye')