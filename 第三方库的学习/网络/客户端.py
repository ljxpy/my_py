#客户端
import threading
import socket
import time
from tkinter import *
def shou():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 8888))
    a0 = "*接收数据进程接入服务器*"
    a = Label(w, text=a0)
    a.place(x=250, y=20)
    c = ''
    while 1:
        cc = ''
        cc = cc+s.recv(1024).decode('utf-8')
        c = c + cc
        if not cc:
            break
        print("从服务器收到的数据为：\n", c[-len(cc):])
def fa():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 8888))
    a0 = "*发送数据进程接入服务器*"
    a = Label(w, text=a0)
    a.place(x=250, y=0)

    def fa1(self):
        c = ''
        c = (c + e1.get()).encode('utf-8')
        s.sendall(c)
    b2 = Button(w, text="发送")
    b2.place(x=400, y=395)
    b2.bind("<Button-1>", fa1)

def b11(n):
    pass
#界面开始
w = Tk()
w.geometry("500x500+500+150")
b1 = Button(w, text="退出程序")
b1.place(x=440, y=0)
b1.bind("<Button-1>", b11)
e1 = Entry()
e1.place(x=250, y=400)


#进程开始
tf = threading.Thread(target=fa)
ts = threading.Thread(target=shou)
tf.start()
time.sleep(0.5)
ts.start()


w.mainloop()