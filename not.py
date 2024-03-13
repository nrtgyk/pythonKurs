vize1notu = int(input("1. vize notunuzu giriniz:"))
vize2notu = int(input("2. vize notunuzu giriniz: "))
finalnotu = int(input("final notunuzu giriniz: "))

notu=((vize1notu*(3/10))+(vize2notu*(3/10))+(finalnotu*(4/10)))


if notu >=90:
    print("harf notunuz AA")
elif 85<= notu<90:
    print("Harf notunuz BA")

elif 80<= notu<85:
    print("Harf notunuz BB")
elif 75<= notu<80:
    print("Harf notunuz CB")
elif 70<= notu<75:
    print("Harf notunuz CC")
elif 65<= notu<70:
    print("Harf notunuz DC")
elif 60<= notu<65:
    print("Harf notunuz DD")
elif 55<=notu<50:
    print("harf notunuz FD")
else:
    print("ders notunuz FF.")
