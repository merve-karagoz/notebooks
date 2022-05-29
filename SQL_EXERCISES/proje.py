from rehber import *     # rehberdeki * bütün kodları çek demek

print(""""************************                 

Rehber Uygulamasına Hoşgeldiniz.

İşlemler:

1. Rehberi Göster:

2. Kişi Sorgulama:

3. Kişi Ekle:

4. Kişi Sil:

5. Arama Sayısı:

Çıkmak İçin 'q' ya Basın:
**************************""")
rehber = Rehber()

while True:
    işlem = input("Yapacağınız İşlem:")
    if (işlem == "q"):
        print("Program Sonlanıyor....")
        print("Yine Bekleriz..")
        break
    elif (işlem == "1"):
        rehber.show_rehber()

    elif (işlem == "2"):
        isim = input("Hangi Kişiyi Görmek İstiyorsunuz:")
        print("Kişi Sorgulanıyor...")
        rehber.search_person(isim)

    elif (işlem == "3"):
        isim = input("İsim:")
        soyisim = input("Soyİsim:")
        telefon_numarasi = input("Telefon Numarası:")
        yas = int(input("Yaş:"))
        arama_sayisi = int(input("Arama Sayısı:"))

        yeni_kisi = rehber_kaydi(isim, soyisim, telefon_numarasi, yas, arama_sayisi)

        print("Kişi Ekleniyor..")


        rehber.kisi_ekle(yeni_kisi)
        print("Kişi Eklendi:")


    elif (işlem == "4"):
        isim = input("Hangi Kişiyi Silmek İstiyorsunuz?")

        cevap = input("Emin misiniz? (E/H)")
        if (cevap == "E"):
            print("Kişi Siliniyor..")

            rehber.kisi_sil(isim)  
            print("Kişi Silindi.")

    
    elif (işlem == "5"):
        isim = input("Kimi Aramak İstiyorsun?")
        print("Arama Sayınız Arttı..")
        rehber.arama_sayisi_artma(isim)    
        print("Aramanız Arttırıldı.")

    else:
        print("Geçersiz İşlem.")