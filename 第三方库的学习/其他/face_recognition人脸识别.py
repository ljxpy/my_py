import face_recognition
import os
import cv2
os.chdir(r'C:\Users\李佳欣\Desktop\py\wo')    #进入当前文件夹
# #定义摄像头
cap = cv2.VideoCapture(0)       #0代表本机摄像头
ret, frame = cap.read()         #拍
cv2.imshow('摄像头', frame)
cv2.imwrite("000.jpg", frame)   #存
cv2.waitKey(1)                  #设置录像帧率
cap.release()   #释放摄像头
cv2.destroyAllWindows() #销毁窗口

images = []
for root, dirs, files in os.walk(r'C:\Users\李佳欣\Desktop\py\wo'):
    #print("root", root)  # 当前目录路径
    #print("dirs", dirs)  # 当前路径下所有子目录
    #print("files", files)   #所有文件
    images = files
images.remove("000.jpg")
print(images)
image_to_be_matched = face_recognition.load_image_file("000.jpg")
image_to_be_matched_encoded = face_recognition.face_encodings(
    image_to_be_matched)[0]
for image in images:
    current_image = face_recognition.load_image_file(image)
    current_image_encoded = face_recognition.face_encodings(current_image)[0]
    result = face_recognition.compare_faces(
        [image_to_be_matched_encoded], current_image_encoded, tolerance=0.4) #阈值
    x, y = image.split(".")
    if result[0] == True:
        print("和%s是同一个人; "%x)
    else:
        print("和%s不是同一个人; " %x)