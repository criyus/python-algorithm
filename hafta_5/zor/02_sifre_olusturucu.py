"""
Güçlü Şifre Oluşturucu:

sifre_uret adında bir fonksiyon yaz.

Parametre olarak uzunluk alsın (varsayılan 8 olsun).

Fonksiyon rastgele harf ve rakamlardan oluşan, belirtilen uzunlukta karmaşık bir şifre return etsin.

İpucu: import random kütüphanesini ve stringleri kullanabilirsin. (Eğer random zor gelirse, manuel bir liste içinden rastgele seçim yapmayı dene).

Alternatif (Random zor gelirse): Kullanıcıdan bir kelime alıp, sesli harfleri sayılarla değiştiren (a->4, e->3, i->1, o->0) basit bir şifreleme fonksiyonu yaz.
"""

import random
import string

def sifre_uret(uzunluk=8):

    karakter = string.ascii_letters + string.digits

    rastgele = "".join(random.choices(karakter,k=uzunluk))

    return rastgele

x = int(input("Şifre Uzunluğu : "))
print("Oluşturulan Şifre :",sifre_uret(x))