import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8000))
s.listen(1)
a, b = s.accept()
print(b, end='')
print("接入服务器")
def fa(x1,x2):
    global a
    if x2 == '1':
        x1 = x1.encode("utf-8")
        a.send('1'.encode('utf-8'))
        a.send(x1)
        hf = a.recv(100)
        print(hf.decode('utf-8'))
    else:
        a.send('2'.encode('utf-8'))
        a.send(x1)
        hf = a.recv(100)
        print(hf.decode('utf-8'))
while 1:
    x = input("发文本or发图？（1 or 2 ?）")
    if x == '1':
        box = input()
        fa(box, '1')
    elif x == '2':
        with open("box.gif", "rb")as f:
            box = f.read()
        fa(box, '2')
    else:
        print("输入错了哎！")