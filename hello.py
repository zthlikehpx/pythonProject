# msg = "hello hpx"
# print(msg)

# import random
# num = random.uniform(1,10)
# print(num)

# str = 'python'
# for i in str:
#     print(i)

# 列表
# L = [1024,0.5,'hello']
# print(L[0])
# print(L[0:])

# L.append('hpx')
# print(L)


# 元组
# 元组是将所有元素都放进小括号中，而列表则是放入中括号
# t = ('d','a','c','h','p','x')

#tuple 列表转换为元组
# d = tuple(L)
# print(d)


# dit = {'name':'小明','age':18}
# dit['name'] = '小红'
# print(dit['name'])

# 将列表转换为字典可用dict函数
# t = [('name','小明'),('age',18)]
# i = dict(t)
# print(i)

# 集合中自动过滤掉相同元素
# s = {'a', 'a', 'b', 'c', 'c'}
# s.clear()
# print(s)



# 函数
# def my_print(name):
    # name = '洪佩旋'
#     print("hi"+name)

# my_print('洪佩旋')


# class Cat:
#     color = 'black'
#     def __init__(self,name):
#         self.name = name
    
#     def eat(self,food):
#         self.food = food
#         print(self.name,'正在吃'+food)


# c= Cat('Tom')
# c.eat('鱼')



# read, 读指定字节
# readlines, 一次读全部
# readline() 一次读一行
# 续读，若上一个已全部读完内容，下一个读取为空
# f = open("D:/测试.txt",mode='r',encoding='utf-8')
# print(f.read(3))
# print(f.readlines())
# wf = open('test.txt',mode='w',encoding='utf-8')

# wf.write('tome,hsisj')
# wf.writelines(['hello\n','python'])
# wf.close()
# f.close()

# count =0
# with open("D:/测试.txt",mode='r',encoding='utf-8') as f :
#     for i in f:
#         line = i.strip()
#         words = line.split(' ')
#         print(words)
#         for i in words:
#             if i =="itheima":
#                 count+=1  
#     print(count)


# 打开已存在的txt，清空原有内容
# 打开不存在的txt，创建文件
# a为追加

# with open("C:/Users/admin/Desktop/测试.txt",mode='a',encoding='utf-8') as f:
#     f.write('hello,hpx')
#     f.flush()

# with open("C:/Users/admin/Desktop/测试.txt",mode='r',encoding='utf-8') as f:
#     with open("C:/Users/admin/Desktop/测试1.txt",mode='w',encoding='utf-8') as fw:
#         for i in f:
#             line = i.strip()
#             # split()之后为列表，不可写出
#             if(line.split(',')[4] == '测试'):
#                 continue
#             fw.write(line)
#             fw.write('\n')


# os 中文就是操作系统的意思，
# Python 的 os 模块提供了各种操作系统的接口
# 这些接口主要是用来操作文件和目录。
# import os
# print("当前路径为"+os.getcwd())


# a = '1024'
# for i in a:
#     print(i)


# 'int' object is not iterable

# 生成器
gen_list =(i for i in range(2,10,3))
print(next(gen_list))
print(gen_list.__next__())
print(gen_list.__next__())
# print(gen_list.__next__())
# print(gen_list.__next__())



# 正则表达式
# group返回字符
# span 返回位置，左闭右开
import re
a = re.match('abc','abcdef')
print(a.span())
print(a.group())

s = """<div>
<p>岗位职责:</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<P>必备要求:</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求:</p>
<p>1、一年以上 Python开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉NVC、MVVM等概念以及相关wEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握SQL，熟练使用 MySQL/PostgresQL中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/cSS/HTML5，JQuery,React.Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项:</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>
</div>"""

a = re.sub(r'<.*?>|&nbsp','',s)
print(a)