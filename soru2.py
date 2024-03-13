a=float(input("a sayısı giriniz: "))
b=float(input("b sayısı giriniz: "))
c=float(input("c sayısı giriniz: "))

if a>b:
    enbuyuk=a
    if a>c:
        enbuyuk=a
    else:
        enbuyuk=c
else:
    if b>c:
        enbuyuk=b
    else:
        enbuyuk=c
print(" en buyuk sayı {} dır.".format(enbuyuk))