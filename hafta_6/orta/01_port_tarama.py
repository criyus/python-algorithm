"""
Port Tarama Sonuçları (Döngü):

Elinizde açık portları gösteren bir sözlük olsun: portlar = {21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS"}

Bir for döngüsü ile (items() kullanarak) ekrana şunu yazdır: "Port 22 üzerinde SSH servisi çalışıyor." (Her port için ayrı satır).
"""


portlar = {
    21: "FTP",
    22: "SSH",
    80 : "HTTP",
    443: "HTTPS"
}


for key, value in portlar.items():
    print(f'Port {key} üzerinde {value} servisi çalışıyor')