
def Selamla(isim="isimsiz"):
    print("Merhaba")
    print("Nasılsınız")
    print("selam",isim)
#Selamla("talha")

def Merhaba(isim):
    print("isminiz: ",isim)
#Merhaba("nurten")

def Sum(a,b,c):
    
    return a+b+c
    """
Sum(3,4,5)


Sum(10,20,30)
"""

def Faktoriyel(sayi):
    faktoriyel=1
    if (sayi==0 or sayi==1):
        print("Faktöriyel: ",faktoriyel)
    else:
        while sayi>1:
            faktoriyel*=sayi
            sayi-=1
        print("faktöriyel: ",faktoriyel)
        """
Faktoriyel(6)
Faktoriyel(0)
"""
def IkiyleCarp(a):
    
    return(a*2)
toplam = Sum(3,4,5)
#print(IkiyleCarp(toplam))

def UcleCarp(a):
    print("1.fonksiyon çalıştı.")
    return a*3
def IkiyleTopla(a):
    print("ikinci fonksiyon çalıştı") 
    return a+2
def DordeBol(a):
    print("3. fonksiyon çalıştı")
    return a/4
    print("çalışmaz")
#print(DordeBol(IkiyleTopla(DordeBol())))

def BilgileriGoster(ad="bilgi yok",soyad="Bilgi yok",numara="bilgi yok"):
    print("Ad:",ad,"soyad:",soyad,"numara",numara)
#BilgileriGoster("Nurten","yıldız")
#BilgileriGoster(numara="1521")

def Toplama(*a):
    print(a)
#Toplama(4,5,6)


def TumToplam(*a):
    toplamlar=0
    for i in a:
        toplamlar+=i
    print(toplamlar)
#TumToplam(1,2,3,7,8,9)
c=10
def Fonksiyon():
    c=2
    print(c)
#Fonksiyon()
#print(c)
#print(a) a globalde değil hata verir.

ikiylecarp = lambda x:x*2
#print(ikiylecarp(3))
topla = lambda x,y,z: x+y+z
#print(topla(10,30,20))


#x=int(input("bir değer griniz: "))
dordebol= lambda x :x/4
#print(dordebol(x))

terscevir= lambda isim:isim[::-1]
#print(terscevir("nurten"))



import math
print(dir(math))