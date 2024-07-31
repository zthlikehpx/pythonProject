class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
#字符串 
    def __str__(self):
        print(f'{self.name},{self.age}')

# 比较
    def __lt__(self,other):
        return self.age < other.age
    
# 等于比较
    def __le__(self,other):
        return self.age <=other.age


# 等等比较 
    def __eq__(self,other):
        return self.age ==other.age

stu =Student('总经理',19)
stu2 = Student('sjha',18)
# print(stu==stu2)


# class MyContextManager:
#     def __enter__(self):
#         print("进入上下文")
#         return self  # 返回的对象会赋值给with语句中的as后面的变量

#     def __exit__(self, exc_type, exc_value, traceback):
#         # exc_type, exc_value, traceback 表示异常信息，
#         # 如果with块中发生异常，这些参数会有值，否则为None
#         print("退出上下文")
#         # 返回True表示处理了异常，返回False表示未处理异常
#         # 如果返回None或False，异常会正常传播
#         return False  # 在这个例子中，我们不处理异常

# # 使用with语句测试上下文管理器
# with MyContextManager() as manager:
#     print("在上下文中执行操作")

# 输出应该是：
# 进入上下文
# 在上下文中执行操作
# 退出上下文

# 编写一个对象，让其支持上下文管理协议（with语句）
class Context():
    def do(self):
        print('222')
    def __enter__(self):
        print('1111')
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print('333')
with Context() as f:
    f.do()
    print('111')
    



