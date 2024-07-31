# # 重写父类
# class Parent:
#     def myMethod(self):
#         print('11')

# class Child(Parent):
#     def myMethod(self):
#         print('223')

# # c = Parent()
# # c.myMethod()

# class Student:
#     school_name = '老男孩'
#     def python(self):
#         pass
#     def linux(self):
#         pass
#     def __init__(self,name,age):
#         self.age = age
#         self.name = name
#         print(name,age)
#     def curr(self):
#         print(f'{self.name}正在选课')
# s = Student('kangkang',12)
# # print(s.school_name)

# # 当名字不存在，新增
# s.hobby = '足球'
# # print(s.hobby)

# class Student:
#     name = '1'
#     def curr(self):
#         print(f'{self.name}正在选课')

# s = Student()
# s.curr()


class Student:
    # 无需实例化，直接通过实例对象.方法名 调用
    @classmethod
    def func(cls):
        print('11',cls)
    
    # 需手动传参
    @staticmethod
    def func2(*args,**kwargs):
        print('11')

Student.func2('aaa','bb')
# Student.func()

class Cat:
    color='black'
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        self.food = food
        print(self.name,'正在吃'+food)



c = Cat('灰灰')
c.eat('鱼')