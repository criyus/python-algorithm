"""
Amaç: Dosya okuma (read/readlines), map() ile veri dönüştürme ve basit analiz.

Senaryo: Bir web sunucusunun log dosyasını (server.log) incelemen gerekiyor. Bazı saldırganlar "Buffer Overflow" (Tampon Bellek Taşması) saldırısı yapmak için sunucuya çok uzun ve anlamsız metinler gönderir. Senin görevin satır uzunluklarını kontrol etmek.

Görev:

Önce kodunun başında, içinde 4-5 satır rastgele veri olan bir server.log dosyası oluştur (bunu kodla yapabilirsin w modu ile).

Dosyayı "okuma modunda" (r) aç.

Tüm satırları bir listeye çek.

map() fonksiyonunu ve len metodunu kullanarak her satırın kaç karakterden oluştuğunu hesapla.

Ekrana "En uzun log kaydı: [X] karakterdir." yazdır.
"""

import random

liste = []
for i in range(10):
    sayi = random.random()
    liste.append(sayi)

with open("./hafta_8/orta/server.log","w") as log:

    a = "\n".join(map(str, liste))
    log.write(a)

with open("./hafta_8/orta/server.log","r") as log:
    
    boyut = list(map(len,log))

print(boyut)