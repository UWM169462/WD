import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns

#
# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
#
# df = pd.DataFrame(ts, columns=['wartosci'])
# print(df)
# df['Srednia kroczaca'] = df.rolling(window=50).mean()
# df.plot()
# plt.legend()
# plt.show()

# x = np.random.randn(10000)
# plt.hist(x, bins=50, alpha=0.75, facecolor='g', density=True)
# plt.xlabel('Wartosci')
# plt.ylabel('Prawdopodobienstwo')
# plt.title('Histogram')
# plt.grid()
# plt.show()

# df = pd.read_csv('dane.csv', header=0, sep=";", decimal='.')
# print(df)
# seria = df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
# wedges, texts, autotext = plt.pie(x=seria, labels=seria.index,
#                                   autopct=lambda pct: "{:.1f}%".format(pct),
#                                   textprops=dict(color="black"),
#                                   colors=['red', 'green'])
#
# plt.title('Suma zamowien dla sprzedawcow')
# plt.legend(loc='lower right')
# plt.ylabel('Procentowy wynik wartosci zamowienia')
# plt.show()

#
# df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
# print(df)
# sns.lineplot(data=df, x=df.index, y='sepal length', hue='class', palette=['yellow', 'pink', 'red'])
# plt.xlabel('indeksy')
# # plt.title('Wykres liniowy danych z Iris dataset')
# plt.show()

data = {'a': np.arrange(20),
        'c': np.random.randint(0, 50, 10),
        'd': np.random.randn(10)}
data['b'] = data['a'] + 10 * np.random.randn(10)
data['d'] = np.abs(data['d'] * 100)
df = pd.DataFrame(data)

plot = sns.relplot(data=df, x='a', y='b', hue='c',
                   palette='bright', size='d', legend=True)
plot.set(xticks=data['a'])
plt.show()
