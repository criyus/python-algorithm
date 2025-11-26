"""
Hava Durumu Önerisi:
Kullanıcıdan sıcaklık değerini (derece olarak) al.
Eğer sıcaklık 20 dereceden büyükse "Tiwheater giyebilirsin", 
20 veya daha düşükse "Montunu almayı unutma" yazdır.
"""

sicaklik = float(input(""))

if sicaklik > 20 :
    print("Tiwheater Giyebilirsin.")
else:
    print("Montunu Almayı Unutma")
