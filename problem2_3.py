def Mukemmel():
    for j in range(0,1000):
        toplam=0
        for i in range(1,j):
    
            if j%i==0:
                toplam+=i
        if toplam==j:
                print("{} mükemmel bir sayıdır.".format(j))
print(Mukemmel())