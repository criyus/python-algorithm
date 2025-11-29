"""
Not Harflendirme:

harf_notu adında bir fonksiyon yaz.

Parametre olarak 0-100 arası bir puan alsın.

Puan 90+ ise "AA", 80-89 ise "BB", 50-79 ise "CC", altı ise "FF" stringi döndürsün.

Kullanıcıdan puanı alıp ekrana "Notunuz: [Harf]" şeklinde yazdır.
"""


def harf_notu(puan):

    if 0 <= puan <= 100:
        if  90 <=puan:
            return "AA"
        elif 80 <= puan <= 89:
            return "BB"
        elif 50 <= puan <= 79 :
            return "CC"
        else:
            return "FF"
    else :
        return "Hatalı Giriş 0-100 Arasında Değer Giriniz!"


xpuan = int(input("Sınav Puanınızı Giriniz: "))

print("Sınav Notunuz : ",harf_notu(xpuan))
