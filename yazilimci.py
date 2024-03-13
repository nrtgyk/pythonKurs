class Yazilimci():
    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara
        self.maas=maas
        self.diller=diller
    def BilgileriGoster(self):
        print("""
        yazılımcı objesinin özallikleri
        isim :{}
        soyisim: {}
        numara:{}
        maas:{}
        diller: {}
        """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller))
    def Zamyap(Self,zamMiktari):
        print("zam yapılıyor.")
        Self.maas+=zamMiktari
    def DilEkle(self,YeniDil):
        print("dil ekleniyor")
        self.diller.append(YeniDil)
Yazilimcinin = Yazilimci("Talha","Gölcügezli",123,3000,["python","C#","C++"])
Yazilimcinin.Zamyap(1500)
Yazilimcinin.DilEkle("java")
Yazilimcinin.BilgileriGoster()