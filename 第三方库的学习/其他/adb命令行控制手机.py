import subprocess
import os
import time

x = os.system(r"D:\新建文件夹\adb安装位置\adb start-server")
print(x)
time.sleep(5)
x = os.system(r"D:\新建文件夹\adb安装位置\adb connect 192.168.1.21")
print(x)
time.sleep(5)
x = os.system(r"D:\新建文件夹\adb安装位置\adb shell input tap 100 100")
print(x)
time.sleep(5)
x = os.system(r"D:\新建文件夹\adb安装位置\adb kill-server")
print(x)


#基本操作（cmd）
'''adb connect 192.168.43.100
adb start-server
adb kill-server
adb tcpip 5555				重启
adb shell input tap 1 1  			点击1，1
adb shell input keyevent <keycode>		按键
adb shell input swipe 1 1 2 2			滑动11 到22
adb push <source> <destination>		复制到手机上	<>只是空格，不输入到命令
adb pull /sdcard/000 D:\\文件名		复制到电脑上
adb shell screencap    -p /sdcard/01.png	截屏到文件夹下
adb shell rm  /sdcard/01.png			删除文件
'''

#网络连接时计算机积极拒绝：
'''adb root        adb shell       setprop service.adb.tcp.port 5555       exit
adb tcpip 5555      adb connect 192.168.1.181
无法连接的原因是安卓系统未打开adb网络调试功能, 通过usb方式连接到安卓系统并设置即可。'''


#详细用法
'''1. 关闭adb服务：adb kill-server
　　2. 启动adb服务  adb start-server
　　3. 查询当前运行的所有设备  adb devices
　　4. 可能在adb中存在多个虚拟设备运行 可以指定虚拟设备运行  -s 虚拟设备名称 
　　5. 重启设备 adb reboot  --指定虚拟设备   adb -s 设备名称 reboot
　　6. 查看日志  adb logcat  清除日志 adb logcat -c
　　7. 进入linux shell下  adb shell 其中常用的linux命令  cd  cat 等等 输入su可以获取超级管理员名称了 要确定是否有哪些命令 进入 system/bin目录 就知道了
 　　8. 传入文件到设备中 adb push 本地文件 远程目录  
　　9. 从设备中拷贝文件到本地  adb -s emulator-5556 pull /data/config.ini d:/
　　10. 显示当前运行的全部模拟器：
  　　  adb devices
　　1 安装应用程序：
   　　 adb install -r 123.apk
　　12. 获取模拟器中的文件：
    　　adb pull <remote> <local>
　　13. 向模拟器中写文件：
    　　adb push <local> <remote>
　　14. 进入模拟器的shell模式：
    　　adb shell
　　15. 卸载apk包：
      　　adb shell
      　　cd data/app
      　　rm 123.apk
     　　exit
      　　adb uninstall 123.apk
      　　adb install -r 123.apk
　　16. 查看adb命令帮助信息：
      　　adb help
　　17. 删除系统应用：
      　　adb remount （重新挂载系统分区，使系统分区重新可写）。
      　　adb shell
      　　cd system/app
     　　 rm 123.apk
　　18. 获取管理员权限：
     　　 adb root
　　19、复制文件： 
     　　复制一个文件或目录到设备： 
     　　adb push <source> <destination></destination></source> 
      　　如：adb push update.zip /sdcard/ 
    　　 从设备上复制一个文件或目录： 
     　　adb pull <source> <destination></destination></source> 
     　　如：adb pull /sdcard/update.zip.
　　20、取得当前运行设备的实例的列表及每个实例的状态： 
    　　adb devices
　　21：adb shell input tap
　     这条命令模拟Android手机在屏幕坐标（X,Y）处进行了点击操作。
 　　22：adb shell input swipe 
     　　这条命令模拟Android手机从屏幕坐标（X1,Y1）滑动到坐标（X2,Y2）的操作。
　　23、uiautomator dump   dump: creates an XML dump of current UI hierarchy 这个命令是用来成成当前界面的UI层次，并用XML格式进行展示 。这样就可以获取各个组件的位置了
 　　注：如果PC要想同时控制多台Android手机，必须在adb 后面添加-s
　　例如：adb -s 13b6e4c4 shell input tap 400 400
　　表示对13b6e4c4这台Android手机进行在屏幕上（400,400）坐标位置进行模拟的点击事件。
　　24. 　　能看到设备信息就代表设备已经连接成功了，接下来的命令就是adb install 路径+包名.apk
例如我的安装包放在桌面，那么命令就是adb install C:\Users\hyh\Desktop\XXX.apk
*** adb shell uiautomator dump /mnt/sdcard/window_dump.xml 获得手机当前界面的UI信息，生成window_dump.xml
*** adb shell input text “123” 输入text
举例：
 　　　　1、打开cmd，进入到当前文件夹中，输入命令 adb devices 查看当前与电脑连接的设备（前提是，手机打开usb调试模式），可以查看已连接成功的手机。
　　　　2、 若手机成功连接，输入命令 adb shell input tap 100 100 , 表示点击屏幕上坐标为（100，100）的点，如果不知道需要点击的点的具体位置的话可以在手机开发者模式中设置。
二. adb 模拟按键：
1. 比如使用 adb shell input keyevent <keycode> 命令，不同的 keycode 能实现不同的功能，完整的 keycode 列表详见 KeyEvent，摘引部分我觉得有意思的如下：

keycode
含义
3
HOME 键
4
返回键
5
打开拨号应用
6
挂断电话
24
增加音量
25
降低音量
26
电源键
27
拍照（需要在相机应用里）
64
打开浏览器
82
菜单键
85
播放/暂停
86
停止播放
87
播放下一首
88
播放上一首
122
移动光标到行首或列表顶部
123
移动光标到行末或列表底部
126
恢复播放
127
暂停播放
164
静音
176
打开系统设置
187
切换应用
207
打开联系人
208
打开日历
209
打开音乐
210
打开计算器
220
降低屏幕亮度
221
提高屏幕亮度
223
系统休眠
224
点亮屏幕
231
打开语音助手
276
如果没有 wakelock 则让系统休眠

2. input 命令的一些用法举例
 电源键
 命令：
?
1
adb shell input keyevent 26
执行效果相当于按电源键。
 菜单键
 命令：
?
1
adb shell input keyevent 82
 HOME 键
 命令：
?
1
adb shell input keyevent 3
返回键
命令：
?
1
adb shell input keyevent 4
音量控制
增加音量：
?
1
adb shell input keyevent 24
降低音量：
?
1
adb shell input keyevent 25
静音：
?
1
adb shell input keyevent 164
媒体控制
播放/暂停：
?
1
adb shell input keyevent 85
停止播放：
?
1
adb shell input keyevent 86
播放下一首：
?
1
adb shell input keyevent 87
播放上一首：
?
1
adb shell input keyevent 88
恢复播放：
?
1
adb shell input keyevent 126
暂停播放：
?
1
adb shell input keyevent 127
点亮/熄灭屏幕
可以通过上文讲述过的模拟电源键来切换点亮和熄灭屏幕，但如果明确地想要点亮或者熄灭屏幕，那可以使用如下方法。
点亮屏幕：
?
1
adb shell input keyevent 224
熄灭屏幕：
?
1
adb shell input keyevent 223
三、使用python脚本自动运行cmd 命令
 在adb文件夹下建立一个python文件
?
1
2
import os
os.system('adb shell input tap 100 100');
运行脚本，发现与在命令行输入相同语句有同样的效果。
2、也可以使用subprocess.Popen，最简单使用方式如下，设置shell=True，就不会弹出cmd框
?
1
process = subprocess.Popen('adb shell input tap 14 1402',shell=True)
程序实例： 
?
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
#coding:utf-8
#程序功能：可以实现抖音个人页面视频的自动点击，从而自动增加访问量
#思路：抖音主页中两个视频切换点击，可以实现访问量的增加
#使用ADB程序，视频的屏幕坐标可以使用adb shell uiautomator dump命令，获取该页面xml源码后查得
#下述是小米MIX2抖音主页第一个视频和第二个视频的坐标位置
#缺点：运行时不能移动屏幕，后续可以采用获取模块ID号的方式去点击相应的位置
import time
import subprocess
i = 0
#每次操作的间隔时间取决于手机配置，配置越高时间越短
sleep_time = 0.5
while 1:
  #用popen设置shell=True不会弹出cmd框
  process = subprocess.Popen('adb shell input tap 14 1402',shell=True)
  time.sleep(sleep_time)
  process = subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
  time.sleep(sleep_time)
  process = subprocess.Popen('adb shell input tap 375 1402', shell=True)
  time.sleep(sleep_time)
  process = subprocess.Popen('adb shell input keyevent KEYCODE_BACK', shell=True)
  time.sleep(sleep_time)
  #os.system('adb shell input tap 14 1402')
  #os.system('adb shell input keyevent KEYCODE_BACK')
  #os.system('adb shell input tap 375 1402')
  i+=1
  print str(i) + 'clicks have been completed'
 实现原理
Hierarchy Viewer：获得当前手机实时的UI信息，方便用于手机的自动化测试；
python中的subprocess.Popen() 或 Python os模块：调用系统命令；
uiautomator工具：获取界面控件信息；
adb命令：对手机进行操作'''
