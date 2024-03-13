a=int(input("a değeri giriniz: "))
b=int(input("b değeri giriniz: "))
c=int(input("c değeri giriniz: "))
delta=b**2-4*a*c
x1=(-b+delta**(1/2))/(2*a)
x2=(-b-delta**(1/2))/(2*a)
print("{}x^2+{}x+{} denkeleminin kökleri {} ve {} dir.".format(a,b,c,x1,x2))

