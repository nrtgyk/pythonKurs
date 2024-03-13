class Twitter():
    def __init__(self,sysKullanciAdi,sysSifre,gundem,tweet,dm):
        self.sysKullaniciAdi = sysKullanciAdi
        self.sysSifre= sysSifre
        self.gundem = gundem
        self.tweet = tweet
        self.dm =dm
    def GirisKontrol(self,kullaniciAdi,kullaniciSifre):
        if self.sysKullaniciAdi!=kullaniciAdi and self.sysSifre==kullaniciSifre:
            print("Kullanıcı Adı Hatalı")
        elif self.sysKullaniciAdi==kullaniciAdi and self.sysSifre!=kullaniciSifre:
            print("Şifreniz Hatalı")
        elif self.sysKullaniciAdi!=kullaniciAdi and self.sysSifre!=kullaniciSifre:
            print("Kullanıcı Adı ve Şifreniz Hatalı")
        else:
            print("Giriş Başarılı")
    def TweetKontrol(self):
        a=0
        b=1
        for i in self.tweet:
            print("Girdiğiniz",b ,". tweetin karakter sayısı : " ,len(self.tweet[a]))
            a+=1
            b+=1
    def GundemEkle(self,yeniGundem):
        self.gundem.append(yeniGundem)
        print("Twitter Gündem: {}".format(self.gundem))
    def DmSayisi(self):
        print("Okunmamış DM sayınız: {}".format(len(self.dm.items())))

twitter = Twitter("Talha","123",["Dolar","Python"],["Pazartesi sendromu","Kötü bir gün"],{"Ahmet":"Naber kanka?","BBK":"Diğer eğitim ne zaman?"})

twitter.GirisKontrol("a","123")
twitter.TweetKontrol()
twitter.GundemEkle("BBK")
twitter.DmSayisi()


        