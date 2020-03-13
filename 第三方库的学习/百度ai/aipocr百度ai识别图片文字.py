from aip import AipOcr
""" 你的 APPID AK SK """
APP_ID = '18434480'
API_KEY = "nyuPCvphcKBVszSmDLQ8yDDz"
SECRET_KEY = 'H2MFokEAzSNk3kY9mAn7kSfZm8bYt7G7'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
import os
os.chdir(r'C:\Users\李佳欣\Desktop\py\w')    #进入当前文件夹

from PIL import Image
i = Image.open("buluo (2).jpg")
region = i.crop((140, 130, 370, 300))
region.save("000.jpg")

ii = open("000.jpg", "rb")
img = ii.read()

'''options = {}
options["language_type"] = "CHN_ENG"  #语言种类
options["detect_direction"] = "true"  #是否横向
options["detect_language"] = "true"   #是否检测语言
options["probability"] = "true"       #置信度'''
message = client.basicGeneral(img)
c1 = []
#print(message.get("probability"))   #用法儿示例
for i in message.get("words_result"):
    str = i.get("words")
    str = str.replace("l", "1")
    str = int(str)
    c1.append(str)
ii.close()
print(c1)
if c1[0]+c1[1] > 400000:
    print("首长，这个部落不错哎！")


#高精度版
print('高精度版:')
print("{' 'height': 字的身高, width':字的宽度 , 'top': (y)距顶得距离, 'left': (x)距左得距离}")
from aip import AipOcr
APP_ID = '18434480'
API_KEY = "nyuPCvphcKBVszSmDLQ8yDDz"
SECRET_KEY = 'H2MFokEAzSNk3kY9mAn7kSfZm8bYt7G7'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
import os
os.chdir(r'C:\Users\李佳欣\Desktop\py\w')    #进入当前文件夹
from PIL import Image
i = Image.open("buluo (1).jpg")
region = i.crop((140, 130, 370, 300))
region.save("000.jpg")
ii = open("000.jpg", "rb")
img = ii.read()

options = {}
#options["recognize_granularity"] = "big"
#options["language_type"] = "CHN_ENG"
#options["detect_direction"] = "true"
#options["detect_language"] = "true"
options["vertexes_location"] = "true"
#options["probability"] = "true"
f = client.general(img, options)

for i in f.get("words_result"):
    print(i["words"])
    print(i['location'])