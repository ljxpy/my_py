import sqlite3
con = sqlite3.connect("d:\\第一个属于自己的数据库.db")
cur = con.cursor()
cur.execute("insert into book (id,name,cj1,cj2,zcj) values ('27','aa',88,88,100)")
con.commit()    #事务提交
cur.close()
con.close()