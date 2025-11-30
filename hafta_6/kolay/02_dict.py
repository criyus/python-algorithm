"""
Siber Tehdit Sözlüğü (Dict):

tehdit adında bir sözlük oluştur.

Anahtarlar: "tur" (Değer: "DDoS"), "iddet" (Değer: 8), "durum" (Değer: "Aktif").

Bu sözlüğe "kaynak_ip" adında yeni bir anahtar ekle ve rastgele bir IP yaz.

"iddet" değerini 10 yap.

Son halini ekrana yazdır.
"""

tehdit = {
    "tur": "DDOS",
    "iddet": 8,
    "durum": "Aktif",
}


tehdit["kaynak_ip"] = "192.168.1.1"

tehdit["iddet"] = 10

print(tehdit)
