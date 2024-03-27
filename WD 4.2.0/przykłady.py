import numpy as np
print('>inicjalizacja tablicy')
a = np.array([0, 1])
print(a)

print('>nowa inicializacja')
a = np.arange(2)
print(a)
print(":wypisanie typu zmiennej tablicy, ale nie jej elementów")
print(type(a))

print(":wypisanie typu zmiennej elementów tablicy")
print(a.dtype)

print('>nowa inicializacja')
a = np.arange(2, dtype='int64')
print(a)
print(":wypisanie typu zmiennej tablicy, ale nie jej elementów")
print(type(a))
print(":wypisanie typu zmiennej elementów tablicy")
print(a.dtype)

print('>nowa tabela')
b=a.astype('float')
print(b)
print(":wypisanie typu zmiennej elementów tablicy")
print(b.dtype)
print(":wypisanie kształtu tablicy")
print(b.shape)
print(":wypisanie ilości wymiarów tablicy")
print(a.ndim)

print('>nowa tabela')
m = np.array([np.arange(2), np.arange(2)])
print(m)
print(":wypisanie kształtu tablicy")
print(m.shape)
print(":wypisanie typu zmiennej tablicy, ale nie jej elementów")
print(type(m))

print("\n:> nowy set przykładów")
zera = np.zeros((5,5))
jedynki = np.ones((4,4))
print(zera)
print(jedynki)
print(zera.dtype)
print(jedynki.dtype)

pusta = np.empty((2,2))
print(pusta)

poz_1 = pusta[1,1]
poz_2 = pusta[0,1]
print(poz_1)
print(poz_2)

liczby = np.arange(1,2,0.1)
print(liczby)

liczby_lin = np.linspace(1,2,5)
print(liczby_lin)

z = np.indices((5,3))
print(z)

x, y = np.mgrid[0:5, 0:5]
print(x)
print(y)

