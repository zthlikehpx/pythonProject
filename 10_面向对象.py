# 重写父类
class Parent:
    def myMethod(self):
        print('11')

class Child(Parent):
    def myMethod(self):
        print('223')

c = Parent()
c.myMethod()