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

jakasLista = ['a', 3, 4.5, 3, 9, 4]
l = input("podaj element")
for element in lista:
    if pow(int(l), 2) == element:
        print('tablica zawiera kwadrat elementu')
# alt:
if pow(int(l),2) in lista:
    print('found')
