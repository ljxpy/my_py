# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码
#1
'''s = input("请输入一个字符串:")
print("{1}{0}{1}".format(s, (10-len(s)//2)*"="))'''
#2
'''s = input("请输入一个字符串:")
print("{:=^20}".format(s))# ^居中 < > '''
#3
s = 3
print("{b}这个数字是{a:+^10}{c}".format(a=s, b='s', c="!"))
print("%c这个数字是%d%c" % ('s', s, "!"))