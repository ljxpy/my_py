import pyautogui        #to代表去往绝对位置 没有的话就是相对位置
#screenWidth, screenHeight = pyautogui.size()   #返回屏幕大小
#X, Y = pyautogui.position()#返回鼠标位置
#pyautogui.move(50, 50)     #相对移动
#pyautogui.click(x=None, y=None,clicks=2, interval=2,button='left', duration=0,tween=pyautogui.linear)
#鼠标点击（次数，间隔时间，鼠标作用位置，时间）
#pyautogui.rightClick()      #鼠标右键点击
#pyautogui.middleClick()     #鼠标中键点击
#pyautogui.moveTo(100, 200, duration=2)     #向(100，200)移动
#pyautogui.moveRel(400, 500,duration=2)         #鼠标相对移动
#pyautogui.dragRel(100, 100, button='left', duration=2)  #鼠标拖动
#pyautogui.scroll(-1000)             #鼠标轮子滚动

#键盘事件
#pyautogui.press('enter')       #点击enter
#pyautogui.typewrite('hello world!')    #输入字符
#pyautogui.keyDown('a')            #按下一个键位
#pyautogui.keyUp('a')              #松开键位
#pyautogui.hotkey('shift', 'a')     #组合键
#提示信息
#pyautogui.alert(text='This is an alert box.', title='Test')    #提示框
#pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])    #选择框
#a = pyautogui.password('Enter password (text will be hidden)');print(a)#输入框
#a = pyautogui.prompt('input  message');print(a)                        #输入框
#im1 = pyautogui.screenshot();im1.save('my_screenshot.png')    #截图；保存
#im2 = pyautogui.screenshot('my_screenshot2.png')       #截图；保存
#pyautogui.FAILSAFE = True  #保护措施
#pyautogui.PAUSE = 0.5   #为所有的PyAutoGUI函数增加延迟。默认延迟时间是0.1秒。