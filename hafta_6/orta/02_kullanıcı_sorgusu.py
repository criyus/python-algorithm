"""
Kullanıcı Sorgusu (.get() metodu):

Basit bir kullanıcı veritabanı yap: users = {"admin": "12345", "guest": "0000"}.

Kullanıcıdan input ile bir kullanıcı adı iste.

Girilen kullanıcı adının şifresini ekrana yazdır.

Kritik: Eğer kullanıcı sözlükte yoksa program çökmesin (Hata vermesin). .get() metodunu kullanarak, kullanıcı yoksa "Kullanıcı Bulunamadı" yazdır.
"""

users = { 
    "admin": "12345",
    "guest" : "0000"
}

api = input("Kullanıcı Adı Giriniz : ")


print(users.get(api,"Kullanıcı Bulunamadı!"))
