#Zad. 2 Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość

plik=open("Zadanie 1.txt","r")

linia=plik.readlines()

plik.close()

print(linia)
