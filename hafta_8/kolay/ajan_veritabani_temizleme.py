"""
Amaç: map() fonksiyonunu string metotlarıyla (strip, upper) birleştirmek ve temiz veriyi dosyaya yazmak (write).

Senaryo: İstihbarat servisine yeni katılan ajanların kod adları bir listede tutuluyor. Ancak veri girişi yapan memur çok dikkatsiz davranmış; isimlerin başında sonunda boşluklar var ve büyük/küçük harf kuralına uyulmamış.

Görev:

Aşağıdaki "kirli" listeyi al:

Python

ajanlar = ["  boNd ", "  hUnT ", " bourne ", " mAdMax "]
map() fonksiyonu kullanarak önce tüm boşlukları temizle (strip), sonra hepsini BÜYÜK HARF yap (upper).

Temizlenen bu listeyi agents.txt adında bir dosya oluşturup içine kaydet. (Her isim alt alta yazılmalı).

İpucu: Dosyaya yazarken her ismin sonuna \n eklemeyi unutma.
"""


ajanlar = ["  boNd ", "  hUnT ", " bourne ", " mAdMax "]

space_clear = list(map(str.strip,ajanlar))

guncel_liste = list(map(str.upper,space_clear))

with open("./hafta_8/kolay/agent.txt","w",encoding="utf-8") as dosya:

    ekle = "\n".join(map(str,guncel_liste))
    dosya.write(ekle)