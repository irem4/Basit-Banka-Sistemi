class Kullanici:
    def __init__(self, isim, hesap_no, bakiye):
        self.isim = isim 
        self.hesap_no = hesap_no
        self.bakiye = bakiye

    def __str__(self): #kullanıcı bilgilerini oku
        return f"{self.isim} - Hesap No: {self.hesap_no} - Bakiye: {self.bakiye} TL"


class Banka:
    def __init__(self):
        self.kullanicilar = [] #banka kullanıcılarını kaydet

    def hesap_ac(self, isim, hesap_no, bakiye):  #yeni kullanıcı hesabı aç bilgileri tamamla
        yeni_kullanici = Kullanici(isim, hesap_no, bakiye)
        self.kullanicilar.append(yeni_kullanici)
        print(f"{isim} için hesap açıldı. Hesap No: {hesap_no}")

    def para_yatir(self, hesap_no, miktar): #uygn kullanıcı adına belirtilen miktarı hesaba aktar
        kullanici = self.kullanici_bul(hesap_no)
        if kullanici:
            kullanici.bakiye += miktar
            print(f"{miktar} TL yatırıldı. Güncel bakiye: {kullanici.bakiye} TL")
        else:
            print("Hesap bulunamadı!")

    def para_cek(self, hesap_no, miktar): #uygn kullanıcı adına belirtilen miktarı hesaptan çek
        kullanici = self.kullanici_bul(hesap_no)
        if kullanici:
            if kullanici.bakiye >= miktar:
                kullanici.bakiye -= miktar
                print(f"{miktar} TL çekildi. Güncel bakiye: {kullanici.bakiye} TL")
            else:
                print("Yetersiz bakiye!")
        else:
            print("Hesap bulunamadı!")

    def bakiye_sorgula(self, hesap_no): #kullanıcının bakiyesini sorgula veya hesabın olmadığını belirt
        kullanici = self.kullanici_bul(hesap_no)
        if kullanici:
            print(f"Güncel bakiye: {kullanici.bakiye} TL")
        else:
            print("Hesap bulunamadı!")

    
        return None



def main():
    banka = Banka()
    while True:  #döngü ile birlikte seçilen sayıya ve hesap numarasına göre(kategoriyi)koşulunu ver,seçim yaptır işlemleri gerçekleştir(ANA MENÜ)
        print("\n1. Hesap Aç\n2. Para Yatır\n3. Para Çek\n4. Bakiye Sorgula\n5. Çıkış")
        choice = input("Seçiminiz: ")

        if choice == "1":
            isim = input("İsim: ")
            hesap_no = input("Hesap Numarası: ")
            bakiye = float(input("Başlangıç Bakiyesi: "))
            banka.hesap_ac(isim, hesap_no, bakiye)
        elif choice == "2":
            hesap_no = input("Hesap Numarası: ")
            miktar = float(input("Yatırılacak Miktar: "))
            banka.para_yatir(hesap_no, miktar)
        elif choice == "3":
            hesap_no = input("Hesap Numarası: ")
            miktar = float(input("Çekilecek Miktar: "))
            banka.para_cek(hesap_no, miktar)
        elif choice == "4":
            hesap_no = input("Hesap Numarası: ")
            banka.bakiye_sorgula(hesap_no)
        elif choice == "5":
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()

    # class kullanıcı; Kullanıcı sınıfı bankadaki müşterileri tutar. kullanıcıların bilgisi burada mevcuttur.
    #class banka; Banka sınıfı kullanıcıların işlemlerini gösterir