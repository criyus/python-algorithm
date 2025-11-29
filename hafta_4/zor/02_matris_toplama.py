"""
Matris (İç İçe Liste) Toplamı:

Dosyanda zip kullanmışsın, bu harika. Şimdi iç içe listelere bakalım.

Şöyle bir matris tanımla:

Python

matris = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
İç içe 2 tane for döngüsü kullanarak bu matristeki tüm sayıların toplamını hesapla ve ekrana yazdır.
"""


matris = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

toplam = 0

for i in matris:

    for t in i:

        toplam += t

print(toplam)