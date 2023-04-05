import math
import random
# zad1
print('zad1')
A=[1-x for x in range(1,10)]
print(A)
B=[pow(4,x) for x in range(0,8)]
print(B)
C=[x for x in B if x % 2==0]
print(C)
# zad2
print('zad2')
# rand= random.sample(range(100), 10) - też działa ale to chyba nie o to chodziło
rand=[random.randint(0,100) for i in range(10)]
print(rand)
Crand=[x for x in rand if x % 2==0]
print(Crand)
# zad3
print('zad3')
zakupy = {
    "sok ziemiaczany": "litry",
    "herbatka ziołowa": "gramy",
    "śruby 8mm": "sztuki",
    "linka typu spadochronowego":"metry",
    "baterie AAAAAAAAAAA":"sztuki",
    "kabel skretka 8zylowy":"metry",
    "wtyczka RJ-45":"sztuki"
}
print(zakupy)
sztuki= [key for key,value  in zakupy.items()if value=="sztuki"]
print(sztuki)
# zad4
print('zad4')
def troojprostoktn(a,b,c):
    if((a**2)+(b**2) ==(c**2)):
        return "jest prostokatny"
    else:
        return "nie jest prostokatny"
print("dla 2 3 4 ", troojprostoktn(2,3,4))
print("dla 3 4 5 ", troojprostoktn(3,4,5))

# zad5
print('zad 5')

def poleTrapez(a=2,b=3,h=4):
    return (a+b)/2*h
print("dla wartosci domyslnych (a=2, b=3, h=4) pole równe jest ", poleTrapez())
print("dla wartosci a=4, b=3, h=2 pole równe jest ", poleTrapez(4,3,2))

# zad6
print("zad6")

#def iloczynCiag(a=1,b=4, ile=10):
#    for(ile)wynik=