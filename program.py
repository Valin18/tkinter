from util import *








secim = int(input("Eğer Bir Hesabınız Var İse '1' Eğer Bir Hesabınız Yok İse '2' Tuşlayınız: "))

if secim == 1:
        clear()
        print('Programa Hoşgeldiniz.')
        time.sleep(1)
        print("--------------------------------------")
        time.sleep(0.5)
        isim = str(input("Kullanıcı Adınızı Giriniz: "))
        sifre = str(input("Şifrenizi Giriniz: "))
        clear()
        kullanıcı = User()
        isim = kullanıcı.username
        sifre = kullanıcı.password
        kullanıcı.GirisBilgileriYazdır(isim, sifre)
elif secim == 2:
        clear()
        print('Programa Hoşgeldiniz.')
        time.sleep(1)
        print("--------------------------------------")
        time.sleep(0.75)
        isim = str(input("Kayıt Olmak İstediğiniz Kullanıcı Adını Yazınız: "))
        time.sleep(0.25)
        sifre = str(input("Şifre Giriniz: "))
        time.sleep(0.25)
        t_sifre = str(input("Aynı Şifreyi Tekrar Giriniz: "))
        time.sleep(0.7)
        if t_sifre == sifre:
                yeni_kullanıcı = User()
                isim = yeni_kullanıcı.username
                sifre = yeni_kullanıcı.password
                yeni_kullanıcı.KayıtBilgisiYazdır(isim, sifre)
        elif t_sifre != sifre:
                time.sleep(1)
                print("--------------------------------------")   
                print("Girilen Şifreler Aynı Değil.")

else:
    print("Yanlış Rakam.")


    