from aip import AipFace

""" 你的 APPID AK SK """
APP_ID = "18469178"
API_KEY = "GuRlksW59t6xdPGLvHaG37Fi"
SECRET_KEY = 'OW2l2mgfoecAe37iAIzxkgL4haIlP6xC'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)
import os
os.chdir(r'D:\新建文件夹\编程资源库\人脸')
img = open("000.jpg", "rb")
i = img.read()
imageType = "01"
client.detect(i, imageType)