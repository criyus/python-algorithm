"""
Büyük Sayı Tespiti: a = 10 ve b = 20 olsun.
b sayısının a sayısından büyük olup olmadığını ve aynı zamanda b'nin 2'ye tam bölünüp bölünmediğini tek bir satırda and kullanarak kontrol et. 
Sonuç True dönmeli.
"""

a = 10
b = 20

sonuc = b > a and b % 2 == 0

print(sonuc)

