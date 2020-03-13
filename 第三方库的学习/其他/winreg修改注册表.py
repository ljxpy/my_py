import winreg
def autorun():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion")
    #计算机\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
    # 删除键
    #winreg.DeleteKey(key, "666")
    # 删除键值
    #winreg.DeleteValue(key, "IconUnderline")
    # 创建新的
    #newKey = winreg.CreateKey(key, "MyNewkey")
    # 给新创建的键添加键值
    winreg.SetValue(key, "Run", winreg.REG_SZ, r"d:\1.txt")
autorun()