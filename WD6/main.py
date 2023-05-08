import numpy as np

# Zad 1
a = np.array ([2,7,3])
b = np.arange (3)
print('zad 1:', a, "*", b, "=", a*b)
# zad 2
print("zad2:")
c = np.array([
    [2,6,3],
    [7,4,8]
])
d = np.arange(16).reshape(4,4)
print(c)
print(d)
# do dokończenia

# zad 3
print("zad 3:", a, "*", b, "=" a**b )