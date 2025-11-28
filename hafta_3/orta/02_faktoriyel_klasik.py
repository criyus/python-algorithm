"""
Faktöriyel Hesaplama (Klasik):

Kullanıcıdan bir sayı al (örn: 5).

Bu sayının faktöriyelini hesaplayan kodu yaz.

Mantık: 5! = 5 * 4 * 3 * 2 * 1 = 120. (Çarpım için başlangıç değişkenini 0 değil, 1 yapmayı unutma!)
"""

sayi = int(input("Sayı Giriniz : "))

fak = 1

for i in range(1, sayi + 1):
    fak = i * fak
print(fak)