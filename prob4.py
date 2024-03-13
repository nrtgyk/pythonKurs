toplam=0
while True:
    a=input("bir sayı giriniz: ")
    
    if a=="q":
        break
    toplam+=int(a)
print("toplam: {} dır".format(toplam))
