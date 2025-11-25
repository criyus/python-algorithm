""""
Ortalama Hesaplama: vize (40) ve final (60) adında iki değişken tanımla (sayıları sen ata).
 Vizenin %40'ını, finalin %60'ını alıp sonuc değişkenine ata ve ekrana yazdır. (Sonuç float çıkmalı).
"""

vize = int(input("Vize Puanınız: "))
final = int(input("Final Puanınız:"))

vh = vize * 40 / 100
fh = final * 60 / 100

sonuc = vh + fh

print("Yarırıl Ortalamanız :", sonuc)