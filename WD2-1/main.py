lista = [1, 2, 3, 4, 5, 5.6, 'a', [12, 11], 3+2j]
print(lista)
lista.append(8)
print(lista)
lista.insert(4, 7)
print(lista)
lista.pop()
print(lista)
lista.pop(1)
print(lista)
lista.remove(7)
print(lista)
lista.reverse()
print(lista)
lista2 = [6, 4, 8.5, 3.21, 5, 8, 10]
lista2.sort()
print(lista2)
del lista[3]
print(lista)
znaki = 'abcde'
print(znaki[0])
slownik={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'a': 6}
print(slownik)
print(slownik['a'])
slownik .pop('e')
print(slownik)
print(slownik.keys())
print(slownik.values())
import sys
# liczba = input('Wprowadź liczbę: ')
# print(liczba)
# sys.stdout.write('Wprowadź liczbe: ')
# liczba=sys.stdin.readline()
# print(liczba)

# a=int(input())
# b=int(input())
# if a>b:
#     print(a)
# else :
#     print(b)
# if a==b:
#     print(a+b)
# else:
#     print('liczby nierówne')

# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# if(a>b) & (c>d):
#     print(a+c)
# else:
#     print(b+d)

for i in range(0, 6, 1):
    print(i)
for item in lista2:
    print(item)
else:
    print('koniec?')

licznik =0
while licznik<len(lista2):
    if lista2[licznik]==8:
        break
    print(lista2[licznik])
    licznik+=1
else:
    print('koniec listy')

# jakasLista = ['a', 3, 4.5, 3, 9, 4]
# l = input("podaj element")
# for element in lista:
#     if pow(int(l), 2) == element:
#         print('tablica zawiera kwadrat elementu')
# # alt:
# if pow(int(l),2) in lista:
    print('found')

# # Zad1
# zdanie=input('podaj zdanie');
# count=1;
# for a in zdanie:
#     if a == ' ':
#         count+=1
# print('zdanie ma ' + str(count) + ' słów')
# # alt (lepsze, bo nie liczy podwójnych spacji):
# print('zdanie ma ' + str(len(zdanie.split())) + ' słów')

# # Zad 2
# sys.stdout.write('podaj trzy liczby')
# a=int(sys.stdin.readline())
# b=int(sys.stdin.readline())
# c=int(sys.stdin.readline())
# sys.stdout.write(str(pow(a,b)+c))

# # Zad 3
# a= input('podaj tekst: ')
# if (a == a[::-1]):
#     print('jest palindromem')
# else:
#     print('nie jest palindromem')

# # Zad 4
# a=int(input('podaj liczbę'))
# for x in range(2, int(a/2+1)):
#     if a%x==0 or a==1:
#         print(str(a) + ' nie jest pierwsza')
#         break
# else:
#     print(str(a) +' jest pierwsza')

# Zad 5
suma = 0
for x in range(1,1000):
    check = 0
    for i in range(1, x):
        if (x % i == 0):
            check = check + i
    if (check == x):
        # print(x)
        suma+=1
print('liczb idealnych do 1000 jest:'+ str(suma))

# Zad 6
lista = [2, 4.20 ,3 ,4, 5, 12.3]
for x in range(len(lista)):
    lista[x]**=2
print(lista)

# # Zad 7
# lista = []
# index = 0
# while index<10:
#     x = input('Podaj liczbę nr ' + index)
#     if