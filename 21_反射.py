"""
去实现某个业务，定义类，类里面封装了很多方法，提供一个统一的入口能够调用各种方法
业务：登录   退出  注册  注销
"""
class Test:
    func_list = ["login","loginOut","register","delete"]
    def login(self):
        print("这是登录")
 
    def loginOut(self):
        print("这是退出")
 
    def  register(self):
        print("这是注册")
 
    def delete(self):
        print("这是注销")
 
    #1.login    2.loginOut  3.register  4.delete
    def run(self,num):
        getattr(self,self.func_list[num-1])()
# num = int(input("请输入你的操作(1.login    2.loginOut  3.register  4.delete):"))
# Test().run(num)
class A:
    name = "bruce"
    def __init__(self):
        self.age = 18
    def eat(self):
        print(f"{self.name} is eating")
        
a = A()
# print(hasattr(a,'age')) #True
# setattr(a,'name','lili') #setattr------修改
# print(getattr(a, "name"))  # bruce
# print(getattr(a, "age"))  # 18
# res = getattr(a, "eat")  # # <bound method A.eat of <__main__.A object at 0x000>>
# res()  # bruce is eating
# getattr(a, "nname") # 报错
# print(getattr(a, "nname", "找不到"))  # 找不到
delattr(A,'name')
print(getattr(a, "name",'找不到'))


import importlib
text = input('输入模块名：')
try:
    module = importlib.import_module(text)
    print('可导入模块')
except ImportError:
    print('不可导入模块')