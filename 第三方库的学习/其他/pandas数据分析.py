from pandas import Series, DataFrame
import numpy

c = [11, 22, 33, 88, 55, 66, 88]
s = Series(data=c, index=range(len(c)))
print(s[:3] + 1)
cc = numpy.array(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
ss = Series(cc)
print(s)
print('------------')
c = {'id': range(201807060201, 201807060204),
     'name': ['a', 'b', 'c'],
     'xingbie': ['n', 'n', 'v'],
     "chengji1": [99, 98, 97],
     'chengji2': [12, 13, 14]
     }
s = DataFrame(c, index=['1', '2', '3'])
print(s.groupby('xingbie').groups)
