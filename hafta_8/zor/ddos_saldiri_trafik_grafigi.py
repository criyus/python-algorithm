"""
Amaç: Veri üretimi, try-except ile hata yönetimi ve matplotlib ile görselleştirme.

Senaryo: Ağındaki trafiği izliyorsun. Son 24 saat içindeki veri trafiğini analiz edip bir saldırı olup olmadığını grafiğe dökmen lazım.

Görev:

Veri Üretme: random kütüphanesini kullanarak 24 saat için (0-24 arası) 0 ile 1000 MB arasında rastgele trafik verisi üret ve bunları traffic_data.txt dosyasına kaydet.

Veri Okuma & Hata Yönetimi:

Bu dosyayı try-except bloğu içinde okumaya çalış.

Dosya bulunamazsa ekrana "Hata: Veri dosyası bulunamadı!" yazsın.

Verileri okuyup bir integer listesine çevir.

Görselleştirme (Matplotlib):

X Ekseni: Saatler (0, 1, 2... 23)

Y Ekseni: Trafik Miktarı (MB)

Grafiği Kırmızı (red) renkte ve Çizgi (plot) grafiği olarak çizdir.

Grafiğe başlık ekle: "24 Saatlik Ağ Trafiği"

plt.show() ile grafiği ekrana getir.
"""


import random
import matplotlib.pyplot as plt

with open("./hafta_8/zor/traffic_data.txt","w") as data:
    for i in range(24):
        trafik_miktar = random.randint(0,100)
        data.write(str(trafik_miktar) + "\n")



try:
    with open("./hafta_8/zor/traffic_data.txt","r") as data:
        traffic_values = []
        satirlar = data.readlines()

        for satir in satirlar:

            temiz_satir = satir.strip()
            sayi = int(temiz_satir)

            traffic_values.append(sayi)
except FileNotFoundError:
    print("Hata: Veri dosyası bulunamadı!")


hours = list(range(24))
plt.plot(hours, traffic_values, color='red')
plt.title("24 Saatlik Ağ Trafiği")
plt.xlabel("Saatler")
plt.ylabel("Trafik Miktarı (MB)")
plt.show()