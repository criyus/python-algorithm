"""
Basit Sayaç (While):

Bir sayac değişkeni 0 olsun.

while döngüsü kullanarak bu sayacı her adımda 5 artır.

Sayaç 50'ye ulaştığında veya geçtiğinde döngüyü durdur ve son değeri ekrana yazdır.
"""

sayac = 0 

while True:
    sayac = sayac + 5
    if sayac >= 50 :
        print(sayac)
        break