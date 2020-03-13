#拍照
import cv2
import time
#定义摄像头
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imshow('000', frame)
cv2.imwrite(r"000.jpg", frame)
cv2.waitKey(1)
cap.release()   #释放摄像头
cv2.destroyAllWindows() #销毁窗口

image = cv2.imread('000.jpg')
print(image.shape)#图的：高,宽
image[1,1] = [200, 200, 200]#修改某一点得像素值
B,G,R = image[1, 1]#获取某一点得像素值
print('B={}, G={}, R={}'.format(B, G, R))
#及其奇怪的坐标表示
y1 = 250;x1 = 250
y2 = 350;x2 = 350
head = image[x1:x2, y1:y2]#对图片得某一位置区域截取   [x1:x2,y1:y2]
image[x1: x2, y1+200:y2+200] = head#给图片某一位置区域赋值                 后边相加向后移动
#cv2.imshow('new1', image)
resized = cv2.resize(image, (400, 400)) #修改图片大小
#cv2.imshow('new2', resized)
output = image.copy()
cv2.rectangle(output, (x1, y1), (x2, y2), (0, 0, 255), 2)#画个红色框
cv2.rectangle(output, (x1+200, y1), (x2+200, y2), (0, 0, 255), 2)        #正常相加向后移
cv2.imshow('new3', output)
cv2.waitKey()
