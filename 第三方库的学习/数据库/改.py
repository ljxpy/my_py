import sqlite3
con = sqlite3.connect("d:/第一个属于自己的数据库.db")
cur = con.cursor()
cur.execute("update book set zcj = zcj + 1 where name = 'z'")
cur.close()
con.commit()
con.close()