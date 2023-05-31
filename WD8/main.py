import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


# plt.plot([1,3,5,7])
# plt.show()

# x= np.array([1,2,3,4])
# y= x**2
#
# plt.plot(x,y, 'ro-')
# plt.axis([0,6,0,20])
# plt.show()
#
# plt.plot(x,y, 'r')
# plt.plot(x,y, 'o')
# plt.axis([0,6,0,20])
# plt.show()

# x = np.arange(0, 5, 0.2)
# plt.plot(x, x, 'r--', x, x**2, 'bo', x, x**3, 'g^')
# plt.legend(labels=['liniowa', 'kwadratowa', 'sześcienna'])
# plt.show()
# plt.plot(x, x, 'r--' label='liniowa')
# plt.legend(loc='center left')

# x = np.arange(0, 10.1, 0.1)
# plt.plot(x, np.sin(x), 'r--' label='sinus')
# plt.xlabel('wartości x')
# plt.ylabel('wartości sin(x)')
# plt.title('wykres sin(x)')
# plt.show()

# data = {'a' : np.arange(50),
#         'c' : np.random.randint(0, 50, 50),
#         'd' : np.random.randn(50)
# }
# data['b'] = data['a']+10*np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
#
# plt.scatter('a','b', c='c', s='d', data=data)
# plt.xlabel('klucz a')
# plt.ylabel('klucz b')
# plt.show()

x1= np.arange(0,2,0.02)
x2= np.arange(0,2,0.02)
y1=np.sin(x1*np.pi*2)
y2=np.cos(x1*np.pi*2)
#
# plt.subplot(4,1,1)
# plt.plot(x1,y1)
# plt.title('Wykres sin(x)')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
#
# plt.subplot(4,1,4)
# plt.plot(x2,y2,'r')
# plt.title('Wykres cos(x)')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.subplots_adjust(hspace=0.5)
# plt.show()

# fig, axs = plt.subplots(3,2)
# axs[0,0].plot(x1,y1)
# axs[0,0].set_title('wykres sin(x)')
# axs[0,0].set_xlabel('x')
# axs[0,0].set_ylabel('sin(x)')
#
#
# axs[1,1].plot(x2,y2)
# axs[1,1].set_title('wykres cos(x)')
# axs[1,1].set_xlabel('x')
# axs[1,1].set_ylabel('cos(x)')
#
# axs[2,0].plot(x1,y1, 'r')
# axs[2,0].set_title('wykres sin(x)')
# axs[2,0].set_xlabel('x')
# axs[2,0].set_ylabel('cos(x)')
#
# fig.delaxes(axs[1,0])
# fig.delaxes(axs[2,1])
# fig.delaxes(axs[0,1])
#
# plt.show()




# ts = pd.Series(np.random.randn(100))
# ts=ts.cumsum()
# ts.plot()
# plt.show()

