a=input("bir sayı giriniz:")
b=len(a)
toplm=0
for i in range(0,b):
    c=int(a[i])
    toplm+=c**b
if toplm==int(a):
    print("{} bir armstrong sayıdır.".format(a))
else:
    print("{} armstrong sayı değildir.".format(a))

