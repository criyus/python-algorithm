"""
Basit Giriş Kontrolü (Login):

Sistemde kayıtlı şifre 1234 olsun.

Kullanıcıdan bir şifre girmesini iste (input).

Eğer girilen şifre 1234 ise ekrana "Giriş Başarılı", değilse "Hatalı Şifre" yazdır.
"""

sifre = 1234

x = int(input("Şifrenizi Giriniz"))

if sifre == x :
    print("Giriş Başarılı.")
else:
    print("Hatalı Şifre.")
