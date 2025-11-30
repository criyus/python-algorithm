"""
Frekans Analizi (Kriptografi Temeli):

Kullanıcıdan uzun bir cümle veya rastgele harflerden oluşan bir string iste (örn: "kriptoloji ve siber güvenlik").

Bu cümledeki her harfin kaç kez geçtiğini hesaplayan bir kod yaz.

Sonuçları bir sözlükte tut.

Örnek Çıktı: {'k': 2, 'r': 2, 'i': 3, ...}

İpucu: Boş bir sözlük oluştur. String üzerinde döngü kur. Harf sözlükte varsa değerini 1 artır, yoksa değerini 1 olarak ekle.
"""

veri = input("Metin Giriniz: ")

frekans = {}


for ch in veri.lower():
    if ch.isspace():
        continue
    frekans[ch] = frekans.get(ch, 0) + 1
print(frekans)