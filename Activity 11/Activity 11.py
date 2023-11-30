hyp=float(input("Enter Length of Hypotenuse : "))
base=float(input("Enter Length of Base : "))
per=float(input("Enter Length of Perpendicular : "))

x=((base**2)+(per**2))**0.5

if x==hyp:
    print("The triangle is Rigth angled Triangle")
else:
    print("The triangle is not Rigth angled Triangle")

s=(hyp+base+per)/2
a=s*(s-hyp)*(s-base)*(s-per)
if a>0:
    area=a**0.5
    print("Area using Heron's formula : ",area)
else:
    print("Triangle is not valid for finding Area.")