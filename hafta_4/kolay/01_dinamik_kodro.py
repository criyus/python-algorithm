"""
Dinamik Kadro Oluşturma:

Boş bir kadro listesi oluştur.

Kullanıcıdan input() ile 3 tane futbolcu (veya sevdiğin bir alanla ilgili isim) girmesini iste ve bunları .append() ile listeye ekle.

Son adımda listenin 2. elemanını (indeks 1) sil (.pop() veya .remove() kullan) ve son halini ekrana yazdır.
"""

kadro = []

for i in range(1,4):
    kadro.append(input(f'{i}. Oyuncuyu Giriniz : '))

kadro.pop(1)
print(kadro)
