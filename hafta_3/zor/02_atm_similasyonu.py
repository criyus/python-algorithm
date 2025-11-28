"""
ATM Simülasyonu (While & If):

Başlangıç bakiyesi 1000 TL olsun.

Sonsuz bir while döngüsü kur (while True:).

Kullanıcıya sor: "İşlem seçiniz: (1) Bakiye Sorgula, (2) Para Yatır, (3) Para Çek, (q) Çıkış".

1: Bakiyeyi göster.

2: Yatırılacak tutarı iste ve bakiyeye ekle.

3: Çekilecek tutarı iste. Eğer bakiye yetiyorsa düş, yetmiyorsa "Bakiye yetersiz" de.

q: Döngüyü sonlandır (break) ve "Güle güle" yaz.
"""

bakiye = 1000

while True:
    print("\n----------------ATM----------------")
    print("------------İşlem Seçiniz------")
    print("(1) Bakiye Sorgula \n (2) Para Yatır \n (3) Para Çek \n (q) Çıkış ")
    
    islem = input("İşlem Seçiniz : ")


    if islem == "1":
        print(f'Güncel Bakiyeniz: ${bakiye}')
    elif islem == "2":
        tutar = int(input("Yatırılacak Tutarı Giriniz : "))
       
        bakiye = bakiye + tutar 
        print(f'Para yatırıldı. Yeni Bakiyeniz: ${bakiye}')
    elif islem == "3":
        cekilecek_tutar = int(input("Çekmek İstediğiniz Tutar : "))  
        if cekilecek_tutar > bakiye:
            print("HATA: Yetersiz Bakiye! İşlem gerçekleştirilemedi.")
        else:

            bakiye = bakiye - cekilecek_tutar
            print(f'Para çekildi. Kalan Bakiyeniz: ${bakiye}')
    elif islem == "q":
        print("Güle Güle, yine bekleriz.")
        break
    else:
        print("Hatalı Giriş! Lütfen tekrar deneyiniz.")