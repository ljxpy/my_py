import sqlite3
con = sqlite3.connect("d:/第一个属于自己的数据库.db")
cur = con.cursor()
cur.execute("delete from book where name = 'aa'")
cur.close()
con.commit()
con.close()