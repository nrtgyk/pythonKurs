ucgenmidortgenmi=input("üçgenin mi dörtgenin mi tipini bulmak istiyorsunuz:")
if ucgenmidortgenmi=="dortgen":
    a=input("1. kenarı giriniz:")
    b=input("2. kenarı giriniz:")
    c=input("3. kenarı giriniz:")
    d=input("4. kenarı giriniz:")
    if a==b==c==d:
        print("bu dörtgen karedir.")
    elif (a==c) and (b==d):
        print("bu dikdörtgendir.")
    else:
        print("bu dörtgendir.")
elif ucgenmidortgenmi=="ucgen":
    e=input("1. kenarı giriniz:")
    f=input("2. kenarı giriniz:")
    g=input("3. kenarı giriniz:")
    if e==f==g:
        print("eşkenar üçgendir.")
    elif e==f or f==g or e==f or e==g:
        print("ikizkenar üçgendir.")
   
    elif e==0 or f==0 or g==0:
        print("bu bir üçgen değildir.")
    elif e!=f and f!=g:
        print("çeşitkenar üçgendir.")


