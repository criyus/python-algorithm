"""
Basit Hesap Makinesi:

Kullanıcıdan iki sayı al (sayi1, sayi2).

Kullanıcıdan yapmak istediği işlemi sor (islem: "+", "-", "*", "/").

if-elif kullanarak seçilen işleme göre sonucu hesaplayıp ekrana yazdır.

Ekstra: Eğer kullanıcı geçersiz bir işlem girerse "Geçersiz İşlem" uyarısı ver.
"""

sayi1 = float(input("Birinci Sayıyı Giriniz."))

sayi2 = float(input("İkinci Sayıyı Giriniz."))

islem = input("Yapmak İstediğiniz İşlemi Giriniz("+", "-", "*", "/")")

if islem == "+":
    print(sayi1 + sayi2)
elif islem == "-":
    print(sayi1 - sayi2)
elif islem == "*":
    print(sayi1 * sayi2)
elif islem == "/":
    print(sayi1 / sayi2)
else:
    print("Geçersiz İşlem.")
