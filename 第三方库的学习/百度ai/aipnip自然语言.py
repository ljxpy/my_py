from aip import AipNlp
import time
import matplotlib.pyplot as ppp
""" 你的 APPID AK SK """
APP_ID = '18558105'
API_KEY = 'CpSXGWHzcAR5SLmOt4VZbWQO'
SECRET_KEY = '510iBgNLmlk3GIzoqIh5EeQFN2PlSmr2'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
""" 调用情感倾向分析client.sentimentClassify(text) """
'''text是string输入的文本内容
items是array输入的词列表
+sentiment是number表示情感极性分类结果, 0:负向，1:中性，2:正向
+confidence是number表示分类的置信度
+positive_prob是number表示属于积极类别的概率
+negative_prob是number表示属于消极类别的概率'''
text = []
f = open("jilu.txt", "r", encoding="utf-8")
lins = f.readlines()
for i in range(len(lins)):
    if lins[i][0:4] == '2020'and lins[i][-3:-1] != r'韵美' and lins[i+1][:1] != '[':
        c = lins[i+1][:-1]
        text.append(c)
f.close()
huatuy = []
huatux = []
for i in range(50):
    try:
        c = client.sentimentClassify(text[i])
        print("%d--%s--%s" % (i, text[i], c['items'][0]['positive_prob']))
        huatux.append(i)
        huatuy.append(float("%0.3f"%c['items'][0]['positive_prob']))
        time.sleep(0.3)
    except:
        huatux.append(i)
        huatuy.append(0.5)
        print("!!!!!!!!!!!!!!!!!!!!!")
        continue
ppp.figure(1, figsize=(8, 4))
ppp.plot(huatux, huatuy, 'r--', linewidth=1.0)
ppp.show()