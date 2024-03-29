import numpy as np
#inicjalizacja tablicy
a = np.array([[0, 1], [2, 3]])
print(a)
#lub drugi sposób
a = np.arange(2, 5, 0.1)
print(a)
#wypisanie typu zmienej tablicy (nie jej elementów)
print(type(a))
#sprawdzenie typu danych tablicy
print(a.dtype)
#inicjalizacja tablicy z konkretnym typem danych
a = np.arange(2, dtype='int64')
print(a.dtype)
#zapisywanie kopii tablicy jako tablicy z innym typem
b = a.astype('float')
print(b)
print(b.dtype)
#wypisanie rozmiaru tablicy
print(b.shape)
#można też sprawdzić ilość wymiarów tablicy
print(a.ndim)
#stworzenie tablicy wielowymiarowej może wyglądać tak
#parametrem przekazywanym do funkcji array jest obiekt,
#może to być pythonowa lista
m = np.array([np.arange(2), np.arange(2)])
print(m.shape)
#ponownie typem jest ndarray
print(type(m))

#3 rodzaje tablic
zera = np.zeros((5, 5), dtype='int32')
jedynki = np.ones((4, 4))
print(zera)
print(jedynki)
#warto sprawdzić jaki jest domyslny typ danych takich tablic
print(zera.dtype)
print(jedynki.dtype)
#można również stworzyć "pusta" macierz o podanych wymiarach
#wartości umieszane są losowo, najpierw podawana jest
pusta = np.empty((2, 2))
print(pusta)
#przez indexy
macierz = np.array([[12, 11], [2, 1]])
print(macierz)
#do elementów tablicy możemy odwołać się tak jak do elementów
poz_1 = macierz[1, 1]
poz_2 = macierz[0][1]
print(poz_1)
print(poz_2)
#tworzenie macierzy 2x2 wraz z uzupełnieniem
macierz2 = np.array([[1,2],[3,4]])
print(macierz2)
#funcka arange potrafi także tworzyć ciągi liczb zmiennych
liczby = np.arange(1,2,0.1)
print(liczby)
#podobnie działa funkcja linspace, które działanie jest
liczby_lin = np.linspace(1,2,5, endpoint=False)
print(liczby_lin)
#a teraz możemy utworzyć dwie macierze, najpierw wartości
z = np.indices((5, 3))
print(z)
print(z[0][1][2])
#podobnie jak w matlabie możemy tworzyć macierze diagonalną
mat_diag = np.diag([a for a in range(5)], k=1)
mat_diag = np.diag([a for a in range(5)], k=-1)
print(mat_diag)
#
mat_diag_k = np.diag([a for a in range(5)], 1)
print(mat_diag_k)
#nump 1wymiarowa
z = np.fromiter(range(5), dtype='int32')
print(z)
#znaki
znaki = b'ogolna'
z1 = np.frombuffer(znaki,dtype='S1')
print(z1)
z2 = np.frombuffer(znaki,dtype='S2')
print(z2)
#
znaki = 'ogolna'
z3 = np.array(list(znaki))
z4 = np.array(list(znaki), dtype='S1')
z5 = np.array(list(b'ogolna'))
z6 = np.fromiter(znaki,dtype='S1')
print(z3)
print(z4)
print(z5)
print(z6)
#
a = np.arange(10)
print(a)
s = slice(2,7,2)
print(a[s])
s = range(2,7,2)
print(a[s])
#możemy ciąć tablice również w sposób znany z cięcia linii
print(a[2:7:2])
#lub
print(a[1:])
print(a[2:5])
#
mat = np.arange(25)
#jednowymiarowa w macierz
mat = mat.reshape((5,5))
print(mat)
print(mat[1:]) #od 2 wiersza
print(mat[:, 1]) #2 kolumna jako wektor
print(mat[:, -1]) #ostatnia kolumna
print(mat[2:5, 1:3]) #2 i 3 kolumna dla 3,4,5 wierszy
print(mat[:, [2,4]]) # 3 i 5 kolumna
print('')
#wierzcholki macierzy
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows,cols]
print(y)
###
#ZAD1
arr = np.arange(20) * 4
print(arr)
#ZAD2
lst_float = [1.2, 2.3, 3.4, 4.5, 5.6]
lst_int32 = np.array(lst_float, dtype='int32')
print(lst_int32)
#ZAD3
def podwa(n):
    return np.array([2 ** i for i in range(n*n)]).reshape((n, n))
print(podwa(3))
#ZAD4
def generuj(base, n):
    return np.logspace(0, n-1, n, base=base)
print(generuj(2, 4))
