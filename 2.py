# social_engineering_scoring.py

keywords = {
    "işten çıkarılma": 20,
    "uygunsuz fotoğraf": 15,
    "şirket": 10,
    "iş yeri": 10,
    "tehdit": 15,
    "geri dönüş": 10,
    "gizli": 20,
    "hassas": 15,
    "indirme": 10,
    "link": 10,
    "yardım": 10
}

formal_words = ["sayın", "saygılarımla", "bilginize", "resmi", "dikkatinize"]
friendly_words = ["selam", "merhaba", "bak", "abi", "kanka", "dostum"]
persuasive_words = ["acil", "önemli", "lütfen", "hemen", "şimdi"]

def puan_hesapla(metin):
    puan = 0
    metin = metin.lower()
    
    # Anahtar kelimeler
    for kelime, deger in keywords.items():
        if kelime in metin:
            puan += deger

    # Resmi kelimeler puan düşürsün
    for kelime in formal_words:
        if kelime in metin:
            puan -= 10

    # Arkadaşça kelimeler ekstra puan
    for kelime in friendly_words:
        if kelime in metin:
            puan += 10

    # İkna edici kelimeler ekstra puan
    for kelime in persuasive_words:
        if kelime in metin:
            puan += 5
    
    # Puan negatif olmasın
    if puan < 0:
        puan = 0

    return puan

def main():
    print("e porta göndrme sunucusu")
    print("Lütfen sosyal mühendislik amaçlı e-posta metnini yazınız:\n")
    print("(Bitirmek için boş satır girin)")

    email_text = ""
    while True:
        satir = input()
        if satir.strip() == "":
            break
        email_text += satir + " "

    toplam_puan = puan_hesapla(email_text)
    print(f"\nToplam Puanınız: {toplam_puan}")

    if toplam_puan >= 60:
        print("Tebrikler! Shell erişimi açıldı. 🎉 /tetikle yaz ctf.py ye")
    else:
        print("Başarısız! Daha ikna edici ve samimi bir e-posta yazmalısın.")

if __name__ == "__main__":
    main()
