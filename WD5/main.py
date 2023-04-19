import numpy as np
# #inicializacja
# a=np.array([0,1])
# print(a)
# #lub
# a=np.arange(2,5,0.1)
# print(a)
# #uzyskiwanie typu tablicy
# print(type(a))
# #uzyskiwanie typu danych
# print(a.dtype)
# #inicializacja z konkretnym typem
# a=np.arange(2, dtype='int64')
# print(a.dtype)
# #zapis sopii jako tablicy o innym typie
# b = a.astype('float')
# print(b)
# print(b.dtype)
# #wypisywanie rozmiaru
# print(b.shape)
# #wypisywanie ilości wymiarów
# print(a.ndim)
# #przykład tworzenia tablicy wielowymiarowej
#
# m=np.array([np.arange(2), np.arange(2)])
# print(m.shape)
#
#
#
# zera=np.zeros((5,5))
# jedynki=np.ones((4,4))
# print(zera)
# print(zera.dtype)
# print(jedynki)
# print(jedynki.dtype)
# #pusta tablica jest tak naprawdę wypełniona wartościami losowymi
# pusta=np.empty((2,2))
# print(pusta)
#
#
# macierz = np.array([[12, 11], [2, 1]])
# print(macierz)
#
#
# liczby_lin = np.linspace(1, 2, 5, endpoint=False)
# print(liczby_lin)
# z = np.indices((5,3))
# print(z)
# mat_diag = np.diag([a for a in range(5)])
# print(mat_diag)
# #tablica jednowymiarowa z danego typu danych
# z = np.fromiter(range(5), dtype='int32')
# print(z)
#
# znaki=b'ogolna'
# z1=np.frombuffer(znaki, dtype='S1')
#
#
# znaki = 'ogolna'
# z3 = np.array(list(znaki))
# z4 = np.array(list(znaki), dtype='S1')
# z5 = np.array(list(b'ogolna'))
# z6 = np.fromiter(znaki, dtype='S1')
# print(z3)
# print(z4)
# print(z5)
# print(z6)
#
# #zad1
a=np.arange(4,4*20+1,4)
print(a)
# zad2
a=np.arange(2,5,0.2)
print(a)
b=a.astype('int8')
print(b)

