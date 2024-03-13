def okunuslar(x):
    a=x//10
    b=x%10
    if a==1:
        c="on"
    elif a==2:
        c="yirmi"
    elif a==3:
        c="otuz"
    elif a==4:
        c="kırk"
    elif a==5:
        c="elli"
    elif a==6:
        c="altmış"
    elif a==7:
        c="yetmiş"
    elif a==8:
        c="seksen"
    elif a==9:
        c="doksan"
    if b==1:
        d="bir"
    elif b==2:
        d="iki"
    elif b==3:
        d="üç"
    elif b==4:
        d="dört"
    elif b==5:
        d="beş"
    elif b==6:
        d="altı"
    elif b==7:
        d="yedi"
    elif b==8:
        d="sekiz"
    elif b==9:
        d="dokuz"
    
    for i in range(0,10):
        for j in range(0,10):
            if (i==a) and (b==j):
                print("{} sayısının okunuşu {}{} dur.".format(x,c,d))
print(okunuslar(78))

