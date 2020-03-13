#视频
import cv2
#定义摄像头
cap = cv2.VideoCapture(0)
while(1) :
    ret, frame = cap.read()
    #读取每一帧
    cv2.imshow('shuai ge', frame)
    #显示每一帧
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()   #释放摄像头
cv2.destroyAllWindows() #销毁窗口

