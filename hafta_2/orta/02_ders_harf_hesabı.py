"""
Ders Harf Notu Hesaplama:

Kullanıcıdan 0 ile 100 arasında bir not girmesini iste.

90 - 100 arası: "AA"

80 - 89 arası: "BB"

70 - 79 arası: "CC"

50 - 69 arası: "DD"

50 altı: "FF"

Bu aralıkları kontrol eden kodu yaz.
"""

puan = int(input("Notunuzu Giriniz.(0-100)"))

if puan >= 90:
    print("Notunuz: AA")
elif 90 > puan >= 80:
    print("Notunuz : BB")
elif 80 > puan >= 70:
    print("Notunuz : CC")
elif 70 > puan >= 50:
    print("Notunuz : DD")
else:
    print("Notunuz : FF")