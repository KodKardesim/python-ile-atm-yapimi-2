from os import system
users = {
    "emre": {
        "adi": "Emre",
        "soyadi": "Gazili",
        "şifre": "gaziliemre12",
        "telefonu": 5555555555,
        "bakiyesi": 5500},
    "hakan": {
        "adi": "Hakan",
        "soyadi": "Kaleli",
        "şifre": "+hakankale+",
        "telefonu": 5555555545,
        "bakiyesi": 1000},
    "emir": {
        "adi": "Emir",
        "soyadi": "Üner",
        "şifre": "emirüner01",
        "telefonu": 5555555545,
        "bakiyesi": 7500},
    "mustafa": {
        "adi": "Mustafa",
        "soyadi": "Güzel",
        "şifre": "xxmustix",
        "telefonu": 5555555535,
        "bakiyesi": 10000}
}
while True:
    system("cls")
    print("Kod Kardeşim ATM Uygulaması")
    k_adi = input("Kullanıcı adı : ")
    k_pass = input("Şifresi : ")
    isimler = users.keys()
    if k_adi in isimler:
        if k_pass == users.get(k_adi).get("şifre"):
            username = k_adi
            password = users.get(k_adi).get("şife")
            name = users.get(k_adi).get("adi")
            surname = users.get(k_adi).get("soyadi")
            cash = users.get(k_adi).get("bakiyesi")

            while True:
                system("cls")
                print(f"Hoşgeldiniz {name} {surname}")
                print("""[1] Bakiye Sorgula
                         [2] Para Yatır
                         [3] Para Çek
                         [Q] Çıkış Yap""")
                print("---")
                islem = input("İşlem seçiniz : ")
                if islem == "1":
                    print("Hesabınızda bulunan toplam bakiye : {} TL".format(cash))
                    input("Devam etmek için enter'a bas.")
                elif islem == "2":
                    yatirilanmiktar = int(input("Yatırmak istediğiniz tutar : "))
                    cash += yatirilanmiktar
                    print("İşlem başarılı. Hesabınızdaki toplam para : {} TL".format(cash))
                    input("Devam etmek için enter'a bas.")
                elif islem == "3":
                    cekilecekmiktar = int(input("Çekmek istediğiniz tutar : "))
                    if cekilecekmiktar > cash:
                        print("Yetersiz bakiye!")
                        input("Devam etmek için enter'a bas.")
                    else:
                        cash -= cekilecekmiktar
                        print("İşlem başarılı. Hesabınızdaki kalan para : {} TL".format(cash))
                        input("Devam etmek için enter'a bas.")
                elif islem == "Q" or islem == "q":
                    print("Çıkış yapılıyor.")
                    input("Çıkış yapmak için 'enter'a bas.")
                    break
                else:
                    print("Hatalı seçim. Lütfen yeniden deneyin")
                    input("Devam etmek için enter'a bas.")
        else:
            print("Kullanıcı adı veya şifre hatalı.")
            input("Devam etmek için enter'a bas.")
    else:
        print("Kullanıcı adı veya şifre hatalı.")
        input("Devam etmek için enter'a bas.")



