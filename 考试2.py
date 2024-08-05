# # k='12'
# # d = {"1":"1","2":"2","3":"3","4":'4',"5":'5',"6":'6',"7":'7',"8":8,"9":'9',"12":'12.3'}
# # if k in d.values():
# #     print('k在字典d的值')
# # else:
# #     print('k不在字典d的值')
# # sum = 0
# # for i in d.values():
# #     sum+=float(i)
# # print(sum)

# class Parent(object):
#     x = 2
#     y = {2: "t1"}
#     def test(self):
#         return "parent test"

# class Child1(Parent):
#     def test(self):
#         return super(Child1, self).test()

# class Child2(Parent):
#     def test(self):
#         return "child2 test"

# class Child3(Child1, Child2, Parent):
#     def test(self):
#         return super(Child3, self).test()

# c3 = Child3()
# print(c3.test())

# Child1.x = 1
# c2 = Child2()
# print(Parent.x, Child1.x, Child2.x, c2.x)

# Parent.x = 3
# print(Parent.x, Child1.x, Child2.x, c2.x)

# c2.x = 4
# c2.y[2] = 't2'
# print(Child2.x, c2.x, Child2.y, c2.y)

# Parent.x = 2
# del c2.x
# print(Child2.x, c2.x)

# num = 0
# for i in range(1,101):
#     num +=i
# print('1+2+3...+98+99+100=',num)
# str = 'luffycity'
# print(str[:5])
# print(str[5:])
# stack = [3, 4, 5, 6, 7, 8]
# print(stack.pop(0))
# print(stack.pop(0))
# print(stack.pop())
# print(stack.pop(-3))
# s=[9,1,5,4,5,6,8]
# for i in s:
#     for j in range(0,len(s)-i-1):
#         if s[j]>s[j+1]:
#             s[j],s[j+1] = s[j+1],s[j]
# print(s)

# num = 0
# i = 0
# while i<=100:
#     num+=i
#     i+=1
# print(num)
# nums = [1,3,5,7,9]
# max = nums[0]
# avg = 0
# min = nums[0]
# for i in range(0,len(nums)):
#     if max<nums[i]:
#         max = nums[i]
# print(max)

# for i in range(0,len(nums)):
#     if min > nums[i]:
#         min = nums[i]
# print(min)

# for i in range(0,len(nums)):
#     avg += nums[i]
# print(avg/5)
def num(n):
    if n == 0:
        return 1
    else:
        return n * num(n-1)

print(num(100))