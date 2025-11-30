"""
Sabit Sunucu Ayarı (Tuple):

server_info adında bir tuple oluştur. İçinde sunucu IP'si ("192.168.1.1") ve Port numarası (8080) olsun.

Bu tuple'ın 2. elemanını (Port) değiştirmeye çalış (kod içinde bir alt satırda server_info[1] = 443 yaz).

Hata alacağını biliyoruz. Bu hatayı try-except bloğu ile yakala ve ekrana "Tuple değiştirilemez!" yazdır. (Eğer try-except henüz görmediysen hatayı al ve yorum satırı yap).
"""

server_info = ("192.168.1.1",8080)

try:
    server_info["port"] = 443
    server_info[1] = 443
except:
    print("Tuple Değiştirilemez")
