from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt
x1 = [[1, 2], [2, 5], [3, 4], [4, 5], [5, 8],
      [10, 13], [11, 10], [12, 11], [13, 15], [15, 14]]
km = KMeans(n_clusters=3)
km.fit(x1)
label = km.labels_
x2 = [[9, 6]]
kne = KNeighborsClassifier()
kne.fit(x1, label)
x2_label = kne.predict(x2)          #预测分类
mark = ["or", "ob","og"]
'''for i in range(len(x1)):
	plt.plot(x1[i][0], x1[i][1], mark[label[i]])
plt.plot(x2[0][0], x2[0][1], mark[x2_label[0]], markersize=17)
plt.show()'''

from sklearn.linear_model import LinearRegression
from numpy import array
x1 = array(x1)
model = LinearRegression()
x = x1[:, 0].reshape(-1, 1)
y = x1[:, 1]
print(x)
print(y)
model.fit(x, y)
x1yyuce = model.predict([[10]])      #预测位置
for i in range(len(x1)):
    plt.plot(x1[i][0], x1[i][1], mark[label[i]])
plt.plot([[10]], x1yyuce, "ob", markersize=17)
plt.show()