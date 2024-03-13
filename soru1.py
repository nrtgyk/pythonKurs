boy=float(input("boyunuzu giriniz: "))
kilo=float(input("kilonuzu giriniz: "))
bedenKutleindexi=kilo/(boy*boy)

if bedenKutleindexi<18.5:
    print("Beden ütle indexiniz {} . zayıfsınız.".format(bedenKutleindexi))
elif 18.5<bedenKutleindexi<25:
    print("Beden kütle indexsiniz {}, normal kilodasınız.".format(bedenKutleindexi))
elif 25<bedenKutleindexi<30:
    print("Beden kütle indexsiniz {}, fazla kilolusunuz".format(bedenKutleindexi))
elif bedenKutleindexi>30:
    print("beden kütle indexsiniz {} , üzgünüm ama obezsiniz.".format(bedenKutleindexi))    
