#服务器
import threading
import socket
import time
from tkinter import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8888))
s.listen(5)
def shou(s):
        so, ad = s.accept()
        a0 = "*收获数据进程%s:%s接入服务器*" %(ad)
        a = Label(w, text=a0)
        a.place(x=250, y=80)
        c = ''
        while 1:
            cc = ''
            cc = cc+so.recv(1024).decode('utf-8')
            c = c+cc
            if not cc:
                continue
            print("从%s:%s收到的数据为：\n" % (ad),c[-len(cc):])

def fa(s):
    so, ad = s.accept()
    a0="*发送数据进程%s:%s接入服务器*" % (ad)
    a = Label(w, text=a0)
    a.place(x=250, y=60)
    def fa1(self):
        c = ''
        c = (c+e1.get()).encode('utf-8')
        so.sendall(c)
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

#线程开始
ts = threading.Thread(target=shou, args=(s, ))
tf = threading.Thread(target=fa, args=(s, ))
ts.start()
time.sleep(0.5)
tf.start()

a0 = ("准备中", threading.Thread.is_alive(ts))
a1 = ("准备中", threading.Thread.is_alive(tf))
a2 = ("开始接听...\n")
a = Label(w, text=a0)
a.place(x=250, y=0)
a = Label(w, text=a1)
a.place(x=250, y=20)
a = Label(w, text=a2)
a.place(x=250, y=40)


w.mainloop()