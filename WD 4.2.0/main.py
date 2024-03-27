import numpy as np
#zad1
zad1=np.arange(3,15*3+1,3)
print(zad1)

#zad2
a=np.arange(0,2.7,0.5,dtype='float')
print(a)
print(a.dtype)
zad2=a.astype('int64')
print(zad2)
print(zad2.dtype)

#zad3
def zad3(n):
    return np.array([[i+n*j for i in range(n)] for j in range(n)])
print(zad3(3))

#zad4
def zad4(a,b):
    return np.logspace(1, b, num=b, base=a)
print("zad4")
print(zad4(2,4))

#zad5
def zad5(l):
    wektor=np.arange(l, 0, -1)
    return np.diag(wektor)
print(zad5(3))

#zad6
import sys
sys.stdout.write()