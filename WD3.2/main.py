import math
import random

# Zad1

print(round((pow((math.e**4 + math.log(34,2)),1/3)),2))
print(round(pow(math.log(20) + (math.cos(45)*5/8), 1/3),2))
#                    ^ = ln(20) = log(20, math.e)
print(round(math.log(23,2)+pow(math.sin(34)+5, 1/3),2))
print(round(pow(math.log(32,2)+math.pi+math.sin(56),1/4),2))

# Zad2
def wierza(height):
    pietro = "a"
    if height > 10:
        height = 10
        print("Za wysoko")
    for x in range(height):
        print(pietro)
        pietro = pietro + "a"
    height=0
# print()
wierza(3)
# print()
# wierza(13)

# Zad 3

def piramida(height):
    pietro = "a"
    if height > 10:
        height = 10
        print("Za wysoko")
    for x in range(height):
        print(" "*(height-x-1) + pietro)
        pietro = pietro + "aa"
    height=0
# print()
piramida(3)

# Zad 4

import random

print(random.randint(2,6))
print(random.random())
print(round(random.random(),3))
print(random.randint(2,6) + round(random.random(),3))
print(random.randrange(2,6))
print(random.uniform(0,3))
print(random.randrange(2,3) + random.uniform(0,3))


# Zad 5
def sumWektor(n):
    wektor = [[round(random.uniform(1, n**n),2) for i in range(n)] for i in range(n)]
    print(wektor)
    suma=[]
    for wiersz in wektor:
        suma.append(round(sum(wiersz),2))
    return suma

print(sumWektor(4))