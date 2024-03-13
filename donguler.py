"""
newList=[1,2,3,4,5,6,7]
toplam=0
for i in newList:
    toplam+=i
    print(toplam)
    print("toplam: {} Eleman:{}".format(toplam,i))
print("listedeki elemanların toplamı: ",toplam)
"""
"""
s="python"
for i in s:
    print(i)
    print(i*3)
    """
"""
list_3=[(1,2),(3,4),(5,6),(7,8)]
for eleman in list_3:
    print(eleman)

for i,j in list_3:
    print("i:{} j:{}".format(i,j))

"""
"""
sozluk = {"bir":1,"iki":2,"uc":3}
for i in sozluk:
    print(i)

for eleman in sozluk.values():
    print(eleman)
for i,j in sozluk.items():
    print("anahtar:  {} Değer:{}".format(i,j))

"""
"""
i=0
while i<10:
    print("i: ",i)
    i+=1
j=0
while j<20:
    print("j",j)
    j+=2
"""
"""
a=0
while a<40:
    print("python öğreniyorum")
    a+=1
"""
"""
listFive=[1,2,3,4,5]
index=0
while (index<len(listFive)):
    print("index",index,"Liste elemanı:",listFive[index])
    index+=1
print(*range(0,20))
"""
#print(*range(20,0,-1))
#for sayi in range(1,20):
 #   print("*" * sayi)

"""
i=0
while (i <20):
    print(i)
    if i==10:
     break
    i+=1
"""
"""
i=1
while i<4:
    i+=1
    if i==2:
        continue
    print(i)
"""
"""
i=0
while(i<10):
    if (i==2):
        i+=1
        continue
    print(i)
    i+=1
"""
"""
list_1=[1,2,3,4,5]
list_2=[i**2 for i in list_1]
print(list_2)
list_3=[(1,2),(3,4),(5,6)]
liste_4=[i*j for (i,j)in list_3]
print(liste_4)
"""
"""
list_5=[1,2,3,4,5,6,7,8,9,10]
list_6=[i for i in list_5 if not (i == 4 or i ==9 )]
print(list_6)
"""
list_8=[[1,2,3],[4,5,6,7,8],[9,10,11,12,1,14,15]]
list_9=[x for i in list_8 for x in i]
print(list_9)