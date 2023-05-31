import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
from PIL import Image

# ts= pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# df=pd.DataFrame(ts,columns=['wartości'])
# print(df)
# df['średnia krocząca']=df.rolling(window=50).mean()
# df.plot()
# plt.legend()
# plt.show()

# x=np.random.randn(1000)
# plt.hist(x,bins=50, facecolor='g', alpha=0.75, density=True)
# plt.xlabel('Wartości')
# plt.ylabel('Prawdopodobieństwo')
# plt.title('Histogram')
# plt.grid()
# plt.show()

df= pd.read_csv('dane.csv', header=0, sep=";", decimal=".")
print(df)
seria = df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
wedges, texts, autotext=plt.pie(x=seria, labels=seria.index,
                                autopct=lambda pct: "{:.1f}%".format(pct),
                                textprops=dict(color="black"),
                                colors=['red','green'])
plt.title('Suma zamówień dla sprzedawców')
plt.legend(loc='lower right')
plt.ylabel('procentowy wynik wartości zamówienia')
plt.show()