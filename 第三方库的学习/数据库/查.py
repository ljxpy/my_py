import sqlite3
con = sqlite3.connect("d:/第一个属于自己的数据库.db")
cur = con.cursor()
x = input("输入id：")
cur.execute("select name,zcj FROM  book where id = '{}'".format(x))
print(cur.fetchall())
cur.execute("select * FROM  book")
for i in cur.fetchall():
    print(i)
cur.close()
con.close()