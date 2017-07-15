import sqlite3

conn=sqlite3.connect("mydatabase.db")
# conn=sqlite3.connect(":memory:")

cursor=conn.cursor()

# create table
cursor.execute(""" create table albums (title text, arties text, release text, publisher text, media_type text) """)

# insert one row
cursor.execute(""" insert into albums values ('西游记','吴彦祖','2/4/2017','不知道','Mp3')""")
conn.commit()

# insert many
albums=[('红楼梦','刘德华','3/5/2016','也不知道','Book'),('水浒传','张学友','4/5/3456','知不知道','kindle'),('三国','梁家辉','1/2/3456','还不知道','Book')]
cursor.executemany("insert into albums VALUES (?,?,?,?,?)",albums)
conn.commit()

# select
cursor.execute("select * from albums")
print(cursor.fetchall())

# update
sql="""
update albums set arties='吴承恩' where arties='吴彦祖'
"""
cursor.execute(sql)

cursor.execute("select * from albums")
print(cursor.fetchall())

# delete
sql="""
delete from albums where arties='吴承恩'
"""
cursor.execute(sql)

cursor.execute("select * from albums")
print(cursor.fetchall())


sql="select * from albums where arties=?"
# cursor.execute(sql,[('刘德华'),('张学友')]) # 这个不能得到正确的结果
cursor.execute(sql,[('刘德华')])
print(cursor.fetchall())

for row in cursor.execute("select rowid, * from albums order by arties"):
    print(row)