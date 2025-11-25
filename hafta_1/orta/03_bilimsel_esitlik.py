"""
Bilimsel Eşitlik: 0.00075 sayısını bilimsel notasyonla (e kullanarak) ifade et.
Bu ifadenin normal ondalıklı haline eşit olup olmadığını (==) kodla kontrol et.
"""

deger = 0.00075

# (7.5 × 10^-4)
bilimsel = 7.5e-4

esit = deger == bilimsel

print("Eşit mi ? :",esit)
