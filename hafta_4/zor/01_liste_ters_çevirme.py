"""
Listeyi Manuel Ters Çevirme (reverse YASAK!):

Kullanıcıdan 5 tane kelime alıp bir listeye at.

Hazır .reverse() fonksiyonunu veya [::-1] dilimlemeyi kullanmadan, algoritma kurarak bu listenin elemanlarını ters çevirip yeni bir listeye kaydet.

Girdi: ['elma', 'armut', 'muz'] -> Çıktı: ['muz', 'armut', 'elma']
"""

meyveler = []

tersmeyve = []

for i in range(1,6):
    meyveler.append(input(f'{i}. Meyve : '))


for t in meyveler:

    tersmeyve = [t] + tersmeyve

print(tersmeyve)
    
