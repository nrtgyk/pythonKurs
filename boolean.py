
"""
a=True
print(type(a))

b= bool(14)
c= bool(0)
d= bool(-1)
print(b,c,d,sep="/")
e="mehmet"=="murat"
f="mehmet"!= "murat"
g= 2<4
h=1.8>=2.5
z="zula"<"araba"
print(z,e,f,g,h)
"""
"""
k=1<2
l="murat"=="murat"
m=1.9>2.1
n="araba">"zula"
print(k and n)
"""
"""
a=2
if (a==2):
    print(a)
print("merhaba")

"""
"""
yas=int(input("yasinizi giriniz: "))
if yas<18:
    print("mekana giremezsiniz.")
else:
    print("mekana girebilirsiniz.")
  

sayi=int(input("bir sayi giriniz."))
if sayi<0:
    print("{} sayisi negatiftir.".format(sayi))
else:
    print("{} sayisi pozitiftir.".format(sayi))
"""

islem=input("işlem numarası giriniz: ")
if islem =="1":
    print("işlem 1 gerçekleşti.")
elif islem=="2":
    print("işlem 2 gerçekleşti.")
else: 
    print("geçersiz işlem.")
