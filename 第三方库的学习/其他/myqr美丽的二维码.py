from MyQR import myqr
from MyQR import myqr
myqr.run(words="http://www.baidu.com/",
version=9,
picture="C:/Users/李佳欣/Desktop/1.jpg",
colorized=True,
save_name='01.png',
save_dir="C:/Users/李佳欣/Desktop") #存




'''words：二维码内容，链接或者句子
veision：二维码大小，范围为[1,40]
level：二维码纠错级别，范围为{L,M,Q,H}，H为最高级，默认。
picture：自定义二维码背景图，支持格式为 .jpg，.png，.bmp，.gif，默认为黑白色
colorized：二维码背景颜色，默认为 False，即黑白色
contrast：对比度，值越高对比度越高，默认为 1.0
brightness：亮度，值越高亮度越高，默认为 1.0，值常和对比度相同
save_name：二维码名称，默认为 qrcode.png
save_dir：二维码路径，默认为程序工作路径
'''