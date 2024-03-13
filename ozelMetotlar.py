class Kitap():
    def __init__(self,isim,yazar,sayfasayisi,turu):
        print("init fonksiyonu")
        self.isim=isim
        self.yazar=yazar
        self.sayfasayisi=sayfasayisi
        self.turu=turu
    def __str__(self):
        return "isim: {}\n yyazar: {}\n Sayfa Sayısı: {}\n türü: {} ".format(self.isim,self.yazar,self.sayfasayisi,self.turu)
    def __len__(self):
        return self.sayfasayisi
    def __del__(self):
        print("kitap objesi siliniyor.")
    
    

kitap = Kitap("suç ve ceza","dostoyevski",700,"roman")

print(kitap)
print(len(kitap))
del kitap
#print(kitap)