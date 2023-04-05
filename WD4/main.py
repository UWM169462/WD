#zad1
# a=input('Podaj a')
# b=input ('Podaj b:')
# wynik = pow(a,2)+a*b+pow(b,2)
# plik=open("zadanie1.txt","w")
# plik.write(str(wynik))
# plik.close()
#zad2
def zadanie2(tab1, tab2):
    wynik=[]
    for i in  range(0, len(tab1)):
        wynik.append(tab1[i]+tab2[i])
    return wynik
taba=[1,2,3,4]
tabb=[4,3,2,1]
print("zad2 :",zadanie2(taba,tabb))
#zad3
plik = open("tekst.txt","r")
plik.read(99)
znaki = plik.read(35)
print("zad3:", znaki)
plik.close()
