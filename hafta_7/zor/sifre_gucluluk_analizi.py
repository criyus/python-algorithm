"""
Amaç: String sorgulama metotlarını (isdigit, isalpha, isalnum, len) mantıksal operatörlerle (if-else) birleştirmek.

Senaryo: Kullanıcının girdiği bir şifrenin sisteme uygun olup olmadığını denetleyen bir algoritma yazman lazım.

Görev: Kullanıcıdan bir şifre (değişken olarak tanımlayabilirsin) alan ve aşağıdaki kurallara göre puan veren bir kod yaz.

Kurallar:

Şifre en az 8 karakter olmalı. (Değilse: "Hata: Çok kısa")

Sadece harflerden oluşmamalı (isalpha kontrolü -> False olmalı).

Sadece sayılardan oluşmamalı (isdigit kontrolü -> False olmalı).

Şifre hem harf hem sayı içeriyorsa (isalnum True ise ve yukarıdaki 2-3 kuralı geçmişse) -> "Orta Seviye Şifre"

(Bonus) Eğer şifre boşluk içermiyorsa ama alfanümerik de değilse (yani @, ? gibi özel karakter içeriyorsa) -> "Güçlü Şifre"

Örnek Girdiler ve Beklenen Çıktılar:

"123456" -> "Hata: Sadece sayı olamaz"

"password" -> "Hata: Sadece harf olamaz"

"pass1234" -> "Orta Seviye Şifre"

"Pass?123" -> "Güçlü Şifre" (Çünkü isalnum() False döner ama geçerli karakterler var)
"""


# Kullanıcıdan şifreyi alıyoruz
sifre = input("Lütfen şifrenizi giriniz: ")

# 1. Kural: Uzunluk Kontrolü
if len(sifre) < 8:
    print("Hata: Çok kısa")

# 2. Kural: Sadece harf mi?
elif sifre.isalpha():
    print("Hata: Sadece harf olamaz")

# 3. Kural: Sadece sayı mı?
elif sifre.isdigit():
    print("Hata: Sadece sayı olamaz")

# 4. Kural: Hem harf hem sayı mı? (Orta Seviye)
elif sifre.isalnum():
    print("Orta Seviye Şifre")

# 5. Kural: Bonus (Güçlü Şifre)
else:
    print("Güçlü Şifre")