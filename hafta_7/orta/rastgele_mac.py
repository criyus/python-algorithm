"""
Amaç: random modülü (choice veya randint) ve join metodunu birleştirmek.

Senaryo: Bir ağ saldırı/savunma simülasyonu için sahte cihazlar oluşturman gerekiyor. Her cihaza benzersiz bir MAC adresi lazım. (Örnek MAC: A1:B2:C3:D4:E5:F6)

Görev: Bana rastgele 1 adet MAC adresi üreten bir kod yaz.

İpuçları:

MAC adresleri 6 parçadan oluşur.

Her parça 0-9 arası rakamlar ve A-F arası harflerden (Hexadecimal) oluşur.

list içine olası karakterleri koyup random.choice kullanabilirsin.

Parçaları birleştirmek için join kullanabilirsin.
"""

import random as rdm

havuz = "0123456789ABCDEF"

rastgele = rdm.choices(havuz, k = 12)

parcalar = []

for i in range(6):
    parca = "".join(rdm.choices(havuz, k=2))
    parcalar.append(parca)

mac = ":".join(parcalar)

print(mac)
