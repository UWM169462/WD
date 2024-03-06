import random
# zad1
A = [x-1 for x in range(1, 10)]
print(A)
B = [pow(4, x) for x in range(0, 8)]
print(B)
C = [x for x in B if x % 2 == 0]
print(C)

# Zad2
rand=[random.randint(69,420) for i in range(10)]
print(rand)
randeven = [x for x in rand if x % 2 == 0]
print(randeven)

# Zad3
produkty={"Chleb": "szt",
          "Mleko": "l",
          "Ziemniaki": "kg",
          "Czekolada": "szt",
          "Sok": "l",
          "Jabłka": "kg"}
sztuki= [key for key, value in produkty.items() if value == "szt"]
print(sztuki)

# Zad4
def czyProstokatny(a,b,c):
    if(pow(a,2)+pow(b,2)==pow(c,2)):
        print("jest prostokątny")
        return True
    else:
        print("nie jest porstokątny")
        return False
print("dla 2 3 4 ")
czyProstokatny(2,3,4)
print("dla 3 4 5 ")
czyProstokatny(3,4,5)

# Zad5
def poleTrapezu(a=2,b=3,h=4):
    return h*(a+b)/2
print("dla wartosci domyslnych pole równe jest ", poleTrapezu())
print("dla wartosci a=4, b=3, h=2 pole równe jest ", poleTrapezu(4,3,2))

# Zad6
def ciągIloczyn(a=1,b=4,ile=10):
    # ciąg = [ i*b for i in range(a,ile)]
    # iloczyn = 1
    # for i in ciąg:
    #     iloczyn*=i
    # return iloczyn
    return [ i*b for i in range(a,ile)]
print(ciągIloczyn())
print(ciągIloczyn(2,3,4))

# Zad7
def pierwiastek(a):
    try:
        if(a <0):
            raise ValueError("Liczba ujemna")
        else:
            return pow(a, 1 / 2)
    except ValueError as e:
        print("Błąd pierwiastkowania")
print(pierwiastek(4))
print(pierwiastek(-4))
print(pierwiastek(0))