"""
Amaç: strip, lower, replace ve title metodlarını kullanarak "dirty data" (kirli veri) temizliği yapmak.

Senaryo: Bir kullanıcı sisteme kayıt olurken adını ve soyadını çok dikkatsiz girmiş. Kenarlarda boşluklar var, bazı harfler büyük bazıları küçük ve yanlışlıkla Türkçe karakter yerine yabancı karakterler kullanılmış (örneğin 'ş' yerine '$' basmış).

Görev: Aşağıdaki değişkeni al ve şu hale getir: "Ahmet Yılmaz"

Girdi:

Python

giris = "  aHmET yiLmAz  "
İstenen İşlemler:

Kenardaki boşlukları sil.

Tüm harfleri küçük harfe çevir.

Baş harfleri büyük yap (Title formatı).

(Opsiyonel) Eğer içinde siber güvenlikçi gözüyle "istenmeyen karakter" varsa temizle (Bu soruda sadece standart formatlama yapman yeterli)
"""

giris = "  aHmET yiLmAz  "

x = giris.strip().lower().replace("i","ı").title()

print(x)