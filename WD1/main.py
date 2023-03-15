import math

print('Zad1')

e=math.e
print(pow(e,10))

print(pow(math.log(pow(math.sin(8),2)),1/6))

print(math.floor(3.55))
print(math.ceil(8.40))

print('Zad2')

imie = "MICHAL"
nazwisko = "MARKUSZEWSKI"

imie = imie.lower()
imie=imie.capitalize()
nazwisko = nazwisko.title()
print(imie, nazwisko)

print('zad3')
nucenie="la la la la la la la la la la la la la la la la la"
print(nucenie.count("la"))
print('zad4')
string="gerrymandering"
print(string[1], string[-1])
print('zad5')
print(string.split(", "))
print('zad6')
sznurek = "sznurek"
dryf = 4.2
szesnastka = 0xB00B69
print(sznurek, dryf, szesnastka,"=",hex(szesnastka),"(16)")
print ('zad7')
sport = ["bilard", "poker", "counter strike"]
print(sport)
sport.reverse()
print(sport)
sporty = ["strzelectwo","golf","szermierka"]
sport.extend(sporty)
print(sport)
print('zad8')
skroty={"lol":"Liga Legend", "XD":"Extreme Difficulty"}
print(skroty)
print('zad9')
#klucz - steamid
gry={
    70:"Half-Life",
    440:"Team Fortress2",
    297000:"Heroes of might and magic 3 HD Edition (Restoration of Erathia)",
    570:"Dota2",
    271590:"Grand Theft Auto V"
}
print(gry)
print("zad10")
print("podaj tekst")
scena=input()

print("ilość 'a' w tekście to: ",scena.count("a"))

print("zad11")

