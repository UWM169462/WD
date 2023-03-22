import random
# zad1
rand=[random.randint(0,30) for i in range(10)]
rand=rand*2
plik=open("plik1.txt","w")
plik.write(str(rand))
# zad2
plik=open("plik1.txt","r")
print(plik.read())
plik.close()
# zad3
rand=[random.randint(0,30) for i in range(10)]
with open("plik2.txt","w") as plik:
    for x in range(3):
        plik.write("the end is never \n")
plik=open("plik2.txt","r")
print(plik.read())
plik.close()
