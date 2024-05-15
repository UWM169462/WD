# def zad1():
#     import math
#     for x in range(13, 29+1):
#
#         print(pow(pow(math.e, x) + math.cos(x), 1 / 4))
# # zad1()
# print()
# def zad2(min, max, ile):
#     import random
#     if min > max or ile <= 0:
#         raise ValueError("Nieprawidłowe parametry")
#
#     elementy = [random.randint(min, max) for _ in range(ile)]
#     print(elementy)
#     slownik = {}
#
#     for element in elementy:
#         if element in slownik:
#             slownik[element] += 1
#         else:
#             slownik[element] = 1
#
#     return slownik
# print(zad2(1,20,5))
# print()
# def zad3(nazwa_pliku):
#     try:
#         with open(nazwa_pliku, 'r') as file:
#             wiersze = file.readlines()
#
#             # usuwanie znaczników końca linii, zastępując je pustym ciągiem znaków.
#             wiersze = [wiersz.replace('\n', '') for wiersz in wiersze]
#
#             # obliczanie sumy z wierszy
#             wiersze_suma = []
#             for i in range(len(wiersze)):
#                 wiersz_elementy = wiersze[i].split(" ")  # Podział wiersz na poszczególne elementy
#                 suma = 0
#                 for element in wiersz_elementy:
#                     suma += int(element)  # Zamiana elementó na liczby całkowite
#                 wiersze_suma.append(suma)  # Dodanie sumy do listy wyników
#
#             # obliczanie sumy z kolumn
#             kolumny_suma = []
#             for i in range(len(wiersze[0].split())):
#                 column_elements = [int(wiersze[j].split()[i]) for j in range(len(wiersze))]
#                 # tworzenie kolumny poprzez podział wierszy, pobranie i-tego elementu z każdego wiersza, i zamiana go na liczbę całkowitą
#                 kolumny_suma.append(sum(column_elements))  # sumowanie elementó kolumny i dodawanie sumy do listy
#
#             return sum(wiersze_suma), sum(kolumny_suma)  # zwrot list
#     except FileNotFoundError:
#         print("Plik nie został znaleziony.") # Zabezpieczanie przed błędem przy wcyztywaniu pliku
#     except Exception as e:
#         print("Wystąpił błąd podczas wykonywania funkcji:", str(e)) # zabezpieczenie generyczne
# print(zad3("liczby 1.txt"))
# print()
# def zad4():
#     import sys
#     try:
#         a = float(sys.stdin.readline())
#         h = float(sys.stdin.readline())
#     except UnboundLocalError:
#         print("problem ze zmienną wejścia")
#         return
#     except ValueError:
#         print("Zła wartość na wejśiu")
#         return
#     return a*a*h/3
# # print(zad4())
# print()
# def zad2A(min, max, ile, n):
#     import random
#     try:
#         if ile % n != 0:
#             raise ValueError("Liczba elementów nie jest podzielna przez liczbę wierszy.")
#
#         elementy = [random.randint(min, max) for _ in range(ile)]  # Generowanie losowych elementów
#         krok=int(ile/n)
#         pozycja=0
#         lista=[]
#         # lista = [elementy[i:i+n] for i in range(0, ile, n)]  # Podział na wiersze
#         for i in range(n):
#             temp=[]
#             for j in range(krok+1):
#                 temp.append(elementy[pozycja])
#                 pozycja+=1
#             lista.append(temp)
#         return lista
#     except ValueError as e:
#         print("Błąd:", str(e))
#         return None
# print(zad2A(1,4,6,3))


#nowości chyba
import numpy as np
a=np.arange(12).reshape((3,4))
print(a)

print(a.sum())

print("\n",a.sum(axis=0))
print("\n",a.min(axis=1))
print("\n",a.cumsum(axis=1))

b=np.arange(3)
print("\n",b)
print("\n", np.exp(b))
print("\n",np.sqrt(b))
c=np.array([2.,-1.,4.])
print("\n",np.add(b,c))
print()
for b in a:
    print(b,", ")
a=np.arange(6).reshape((3,2))
print(a)
for b in a.flat:
    print(b,", ")
b=a.reshape((2,3))
print(b)
print(b.shape)
c=b.reshape((3,2))
print(c)
print(c.shape,"\n")

d=c.ravel()
print(d)
