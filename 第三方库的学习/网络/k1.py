import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8000))#free.idcfengye.com
def shouz():
    x = s.recv(500)        #会阻塞进程      #收到必须小于5000，否则下一次recv还会继续接收
    print("服务器：", x[-19:-18])
    s.send("客户端已收到".encode('utf-8'))
def shout():
    a = s.recv(5000)
    with open("shoudao.gif", "wb") as f:
        f.write(a)
    f.close()
    s.send("客户端已收到".encode('utf-8'))
    print("图片已保存")
while 1:
    x = s.recv(10).decode("utf-8")
    if x == '1':
        shouz()
    elif x == '2':
        shout()
    else:
        print("服务器错了哎！!")
        break