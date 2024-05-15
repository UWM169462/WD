# Zad 1
import math
suma = 0
for n in range (10,25+1):
    wynik=pow(pow(math.e,3)+pow(math.cos(n),2),1/5)+pow(2/7,3)+math.pi
    suma += wynik
print("zad1: " + str(round(suma,2)))

# Zad 2
import random
def Zad2(min_val, max_val, count):
    # Sprawdzenie poprawności argumentów
    if min_val > max_val or count >= (max_val - min_val) or count<=0 or count%1!=0:
        print("Niepoprawne argumenty!")
        return {}
    else:
        # Tworzenie listy losowych wartości
        values = random.sample(range(min_val, max_val + 1), count)
        print(values)
        # Tworzenie słownika
        dictionary = {}
        for i in range(0, count, 2):
            if i+1 < count:
                dictionary[values[i]] = values[i+1]
            else:
                dictionary[values[i]] = 0

        return dictionary
print("zad2: " + str(Zad2(2,12,7)))

# Zad 3
# def Zad3(plik):
#     plik=open(plik, "r")
#     print(plik)
#     tekst=plik.read()
#     lines=tekst.split("\n")
#     print(tekst)
#     for line in lines:
#         lines[line]=lines[line].split()
#     print(lines[2,3])


# Zad3("liczby 2.txt")
def compare_sums(nazwa_pliku):
    try:
        # Wczytanie pliku
        with open(nazwa_pliku, 'r') as file:
            lines = file.readlines()
            print(lines)
        # Inicjalizacja list
        first_column = []
        diagonal = []

        # Przetwarzanie danych z pliku
        for line in lines:
            # Podzielenie linii na elementy
            elements = line.strip().split()

            # Sprawdzenie, czy linia ma wystarczającą liczbę elementów
            if len(elements) >= 1:
                # Dodanie pierwszego elementu do listy pierwszej kolumny
                first_column.append(int(elements[0]))

                # Sprawdzenie, czy linia ma wystarczającą liczbę elementów dla przekątnej
                if len(elements) >= len(diagonal):
                    # Dodanie elementu z przekątnej do listy przekątnej
                    diagonal.append(int(elements[len(diagonal)]))
        print("k:"+str(first_column)+" d:"+str(diagonal))
        # Obliczenie sumy elementów dla każdej listy
        sum_first_column = sum(first_column)
        sum_diagonal = sum(diagonal)

        # Sprawdzenie, która suma jest większa i zwrócenie odpowiedniej listy
        if sum_first_column > sum_diagonal:
            return first_column
        else:
            return diagonal

    except FileNotFoundError:
        print("Plik nie istnieje!")
        return []
    except IOError:
        print("Błąd odczytu pliku!")
        return []


# Przykładowe użycie funkcji
nazwa_pliku = "liczby 2.txt"
result = compare_sums(nazwa_pliku)
print("Zad3"+str(result))
# Zad 4
def Zad4(a):
    try:
        # Konwersja wczytanej liczby na liczbę całkowitą
        a = int(a)

        # Obliczenie kombinacji a*(b+c)
        result = a * (6 + 12)

        # Konwersja wyniku do postaci liczby binarnej
        binary = bin(result)
        # Znalezienie numerów bitów równych 0
        zero_bits = [i for i, bit in enumerate(binary[1:]) if bit == '0']

        return zero_bits
    except ValueError:
        print("Niepoprawna wartość! Podaj liczbę naturalną.")
        return []


# Przykładowe użycie funkcji
# input_value = input("Podaj liczbę naturalną: ")
input_value = 4
result = Zad4(input_value)
print("Zad4: " + str(result))