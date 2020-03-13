import sqlite3
def jianli():
    con = sqlite3.connect("d:\\第一个属于自己的数据库.db")
    con.execute("create table book (id char(10), name char(200), cj1 smallint, cj2 smallint, zcj smallint)")
    con.close()
#smallint integer   16位整数32位整数
#float double 32位实数64位实数
#char(n)长度字符串#varchar（n）长度不固定n<=4000
#date 包含了年月日 time包含了时分秒
