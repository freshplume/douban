#-*- codeing = utf-8 -*-
#@Time : 2021/1/4 12:43
#@Author : 杨新羽
#@File : TestSqlite.py.py
#@Software: PyCharm

#1、连接数据库
import sqlite3
conn = sqlite3.connect("test.db") #打开或创建数据库文件

print("成功打开数据库")

c = conn.cursor()   #获取游标

#2、创建数据表
# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real
#         );
# '''
#3、插入数据

sql = '''
    insert into company (id,name,age,address,salary)
    values (NULL,'老王',32,'成都',8000);

'''
# sql1 = '''
#     insert into company (id,name,age,address,salary)
#     values (2,'李四',33,'北京',15000);
# '''
#4、查询数据

# sql = '''
#     select * from company;
# '''

c.execute(sql)  #执行SQL语句

# for row in c:
#     print("id = ",row[0])
#     print("name = ", row[1])
#     print("age = ", row[2])
#     print("address = ", row[3])
#     print("salary = ", row[4],'\n')

# c.execute(sql1)
conn.commit()   #提交数据库操作，只有增删改才需要提交
conn.close()    #关闭数据库连接

print("成功执行")


