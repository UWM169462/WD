#Zadanie 1

a=input("Podaj a: ")
b=input("Podaj b: ")

try:
    wynik = int(a) * int(a) + int(a) * int(b) + int(b) * int(b)
    # wynik=(a*a)+(a*b)+(b*b)
except:
    print("Błąd! Zły typ liczb!")

plik = open("Zadanie 1.txt", "w+")
odp = "Wynik działania a^2+ab+b^2: ", wynik
plik.writelines(str(odp))

plik.close()


#
# Zadanie 2

def sumaliczb(lista1,lista2):
    lista3=[]
    for i in range(0,len(lista1)):
        lista3.append(lista1[i]+lista2[i])
    return lista3

list1=[2,3,4,5,6,7,8,9]
list2=[12,32,47,53,5,78,12,9]

print(sumaliczb(list1,list2))

#Zadanie 3

# Dany jest plik tekst.txt.
# Dokonaj wczytania pliku wraz z obsługą polskich znaków oraz zapisz do zmiennej znaki, 35 znaków z tekstu zaczynając od 100 znaku tekstu.
# Następnie wyświetl duże litery z wczytanego fragmentu oraz ich ilość, jeśli ich nie będzie wyświetl odpowiedni komunikat.

#-*- coding: utf -8  -*-
plik=open('Tekst.txt','r',encoding="utf-8")

dane=plik.read(100)
znaki=''
for i in range(0,35):
    znaki+=dane[i]

ilosc=0
for i in range(0,len(znaki)):
    if znaki[i].isupper==True:
        print(znaki[i])
        ilosc+=1

if ilosc>0:
    print(ilosc)
else:
    print("Nie znaleziono dużych liter!")
plik.close()


#Zadanie 4

lista=[2,3,52,37,24,271,3196,27031]
a=100

d=[lista[i] for i in range(0,len(lista)) if lista[i]>a]
nowa=d

print(nowa)


#Zadanei 5

import math

wynik= math.pow(((math.pow(math.e,3)+(math.cos(39)**2))+((2/7)/3)+math.pi),5)

print(wynik)