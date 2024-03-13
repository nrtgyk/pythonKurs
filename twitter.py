class Twitter():
    def __init__(self,kullaniciİsmi,sifre,tweet,gundem,dm):
        self.kullaniciİsmi=kullaniciİsmi
        self.sifre=sifre
        self.tweet=tweet
        self.gundem=gundem
        self.dm=dm
    def GirisKontrol(self,isim,sifre_1):

        
        if isim==self.kullaniciİsmi and sifre_1==self.sifre:
           print("giriş başarılı")
        else:
            print("giriş başarısız.")
    def TweetAt(self):
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
twitter.GirisKontrol("Talha","123")
twitter.TweetAt()
twitter.GundemEkle("BBK")
twitter.DmSayisi()
