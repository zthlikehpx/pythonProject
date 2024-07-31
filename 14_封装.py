# class Phone:
#     # 私有成员不能被直接使用
#     __current_voltage = 1

#     def __keep(self):
#         print('11')
    
#     # 私有的只能自己使用
#     def call(self):
#         if self.__current_voltage>=1:
#             print('5G牛')
#         else:
#             self.__keep()

# p = Phone()
# # p.__keep()
# # print(p.__current_voltage)
# p.call()


# class Tell:
#     # 无法直接访问,只能通过类里面的方法进行访问
#     __is_5g_enable = True

#     def __check_5g(self):
#         if self.__is_5g_enable == True:
#             print('5g1')
#         else:
#             print('5g no')
    
#     def call(self):
#         self.__check_5g()

# p = Tell()
# p.call()

# class Person:
#     def __init__(self,name,age,title):
#         self.__name = name
#         self.__age = age
#         self.__title = title
#     @property
#     # 类实例化后的对象调用该方法时后面不再需要加上小括号了
#     def school(self):
#         print(self.__age)

# p = Person('hopx',12,'ww')
# p.school



# 伪装
# 注意
    # 内置装饰器函数 只在面向对象中使用
    # 装饰后效果：将类的方法伪装成属性
    # 被property装饰后的方法，不能带除了self外的任何参数
# @property 可以将python定义的函数“当做”属性访问，从而提供更加友好访问方式，但是有时候 setter/deleter 也是需要的。
# 1、只有 @property 表示 只读 。
# 2、同时有 @property 和 @*.setter 表示 可读可写 。
# 3、同时有 @property 和 @*.setter 和 @*.deleter 表示可读可写可删除。

class Person(object):
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
    @property
    def BMI(self):
        return self.weight / (self.height**2)
    
p = Person('jaon',1.64,48)
# 利用 @property 伪装成数据
print(p.BMI)