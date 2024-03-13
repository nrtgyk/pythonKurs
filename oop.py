"""class Araba():
    model ="Ferrari"
    renk ="siyah"
    beygirgücü=580
    silindir=8
    def __init__(self) -> None:
        print("init çağrıldı")

arabaOne= Araba()
print(arabaOne)
#print(arabaOne.silindir)
#print(arabaOne.beygirgücü)
#print(arabaOne.model)
"""
class Araba():
    def __init__(self,model="bilgi yok",renk="bilgi yok",beygirgucu=70,silindir=4):
        print("init çalıştı")
        self.model=model
        self.renk=renk
        self.beygirgucu=beygirgucu
        self.silindir=silindir
arabaone=Araba("citroen","kırmızı",700,8)
print(arabaone.silindir)
arabatwo=Araba("peugout","siyah",110,4)
print(arabatwo.model)

