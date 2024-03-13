a=int(input("bir sayı giriniz:"))
toplam=0
for i in range(1,a):
    
    if a%i==0:
        toplam+=i
if toplam==a:
        print("{} mükemmel bir sayıdır.".format(a))
else:
        print("mükemmel sayı değildir.")
