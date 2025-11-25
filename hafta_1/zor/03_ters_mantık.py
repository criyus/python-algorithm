"""
Ters Mantık (De Morgan): x = 5, y = 10, z = 15. 
Şu ifadenin sonucunun False çıkmasını sağlayan mantıksal operatör dizilimini not, and, or kullanarak yaz: 

"x, y'den küçük DEĞİL VE y, z'den büyük DEĞİL".
"""

x = 5 
y = 10
z = 15

a = not x < y and y < z 

print(a)