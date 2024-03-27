import random
def wektor_nxn(n):
    wektor = []
    for i in range(0, n):
        lista = [random.randint(0, 20) for _ in range(n)]
        wektor.append(lista)
    print(wektor)
    for j in wektor:
        print(j, sum(j))

wektor_nxn(5)