"""
Log Analizi (İç İçe Sözlükler):

Aşağıdaki gibi bir yapı tanımla:

Python

log_kaydi = {
    "tarih": "2025-10-23",
    "kullanici": "root",
    "olaylar": {
        "giris_denemesi": 3,
        "basarili_mi": False,
        "ip_adresleri": ["192.168.1.50", "10.0.0.1"]
    }
}
Bu sözlükten;

Son giriş denemesi yapılan IP adresini (10.0.0.1),

giris_denemesi sayısını çekip ekrana yazdır.
"""

log_kaydi = {
    "tarih": "2025-10-23",
    "kullanici": "root",
    "olaylar": {
        "giris_denemesi": 3,
        "basarili_mi": False,
        "ip_adresleri": ["192.168.1.50", "10.0.0.1"]
    }
}

son_giris = log_kaydi["olaylar"]["ip_adresleri"][1]
deneme_sayisi = log_kaydi["olaylar"]["giris_denemesi"]

print(f'Son Giriş Denemesi Yapılan IP: {son_giris}')

print(f'Giriş Deneme Sayısı : {deneme_sayisi}')