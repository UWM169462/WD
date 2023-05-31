import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# zad 1
# Za pomocą bibliotek matplotlib utwórz wykres liniowy funkcji f(x)=x2 + sin(x), dla 13 wartości x z przedziału [-5,5]. Dodaj odpowiednie etykiety do osi wykresu, tytuł linii, legendę oraz tytuł wykresu. Dodatkowo wyświetl oba wektory przekazywane na wykres. Ustaw zakres oś x na granice przedziału.

x =np.arange(-5,6,11/13)
plt.axis([-5,5,-1,28])
y=(pow(x, 2) + np.sin(x))
plt.plot(x,y, 'ro-')
plt.xlabel("Oś X")
plt.ylabel("Oś wartości f(x)")
plt.title("f(x)=x2 + sin(x)")
plt.legend()
plt.show()
plt.savefig('zad1.png')
print(x)
print(y)

# zad 2
# Za pomocą matplotlib odwzoruj siatkę wykresów z poniższego zdjęcia. Siatkę zapisz do pliku(imie_nazwisko_zad2.png)
x1= np.arange(-2,2.02,0.02)
x2= np.arange(0,2,0.02)
y1 = np.tan(x1) * np.sin(x1)
y2 = np.sin(x2) + np.tan(x2)

fig,axs = plt.subplots(2, 2)
axs[0,1].axis([-2,2,-35,15])
axs[0,1].plot(x1, y1)
axs[0,1].set_title('Pierwszy wykres')
axs[0,1].set_xlabel('x')
axs[0,1].set_ylabel('wynik funkcji')
axs[0,1].legend()
axs[1,0].plot(x2,y2)
axs[1,0].plot(x1, np.tan(x1) * np.sin(x1))
axs[1,0].set_title('drugi wykres')
axs[1,0].set_xlabel('x')
axs[1,0].set_ylabel('wynik funkcji')
axs[1,0].legend()


fig.delaxes(axs[1,1])
fig.delaxes(axs[0,0])
plt.show()
plt.savefig('michal_markuszewski_zad2.png')
# zad 3
# df = pd.read_csv('wine.data')
# ts = pd.DataFrame(df, rows=['1','2'])
#
#

# zad 4
df = pd.read_csv('wine.data')
udzial = df.groupby('Class')['Class'].sum()
plt.pie(udzial, labels=udzial.index, autopct='%1.1f%%')
plt.legend()
plt.show()
plt.savefig('zad4.png')


