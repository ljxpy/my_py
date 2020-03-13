from numpy import *
a = array([1, 2, 30])
print(a)
print(a.dtype)
b = array([1, 3, 5.1])
print(b.dtype)
c = array([1, 2, 3], dtype=complex)
print(c)
print(c+b)
d = array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])
dd = array([[3, 2, 1],
            [5, 4, 3],
            [9, 8, 7]])
print(1111111)
print(dot(d, dd))

