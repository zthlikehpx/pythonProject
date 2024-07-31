# import pymysql
# connect = pymysql.connect(
#     host='localhost',
#     port = 3306,
#     user = 'root',
#     password = '123456',
#     database='text',
#     charset='utf8'
# )
# cusor = connect.cursor()
# sql = 'insert into student(name,age)values(%s,%s);'
# data=[
#     ('大大','52'),
#     ('小王','13')
# ]
# cusor.executemany(sql,data)
# connect.commit()
# cusor.execute('SELECT * from student')
# print(cusor.fetchall())
# cusor.close()
# connect.close()

from peewee import *
db = MySQLDatabase('text',
                    host='localhost',
                    port = 3306,
                    user = 'root',
                    password = '123456',
                    charset='utf8')
class Teacher(Model):
    id = AutoField(primary_key = True)
    name = CharField()
    age = IntegerField()
    class Meta:
        database = db
'''新建表'''
# db.create_tables([Teacher])
'''新增'''
# t1 = Teacher(name = '张三',age=22)
t2 = Teacher(name = '李四',age=26)
# t3 = Teacher(name = '范巽',age=24)
# t4 = Teacher(name = '东方',age=24)
# t1.save()
t2.save()
# t3.save()
# t4.save()
'''查询所有'''
# t = Teacher.select()
# for i in t:
#     print(i,i.name,i.age)
'''查询单条'''
# t = Teacher.get(Teacher.age==33)
# print(t.name)
'''查询多条'''
# t = Teacher.select().where(Teacher.age==24)
# for i in t:
#     print(i,i.name)
'''修改'''
# t = Teacher.update({Teacher.name:'张四'}).where(Teacher.id==1)
# t.execute()
'''删除'''
# Teacher.delete().where(Teacher.id==2).execute()