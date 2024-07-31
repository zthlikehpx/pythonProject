# '''19、编写代码找出以下words序列中出现频率最高的3个单词（写出解题思路得2分）
# words = [ 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'aroun
# d', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under' ]（10分）'''
# # # 定义words列表
# # words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under']

# # # 统计每个单词出现的次数
# # word_count = {}
# # for i in words:
# #     if i in word_count:
# #         word_count[i] += 1
# #     else:
# #         word_count[i] = 1

# # # 按照出现次数排序单词
# # sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# # # 获取出现频率最高的三个单词
# # top_three_words = sorted_word_count[:3]

# # print(top_three_words)


# '''
# 编写代码求以下列表的最大值，最小值，平均值 nums = [1,3,5,7,9]（4分）'''
# # nums = [1,3,5,7,9]


# # max = max(nums)
# # min = min(nums)
# # avg = sum(nums)/len(nums)
# # print(max,min,avg)


# # max = nums[0]
# # min = nums[0]
# # avg = 0
# # for i in nums:
# #     if(max<i):
# #         max=i
# #     if(min>i):
# #         min = i
# #     avg +=i
# # print(max,min,avg/len(nums))  #9 1 5.0


# '''编写代码，使用for循环计算1到100的和（5分）'''
# # num = 0
# # for i in range(0,101):
# #     num +=i
# # print(num)


# ''' 使用while循环计算1到100的和（5分'''
# # num = 0
# # i=1  #要定义i
# # while i<=100:
# #     num +=i
# #     i+=1
# # print(num)


# '''
# 有一列表：items = [0,1,2,3,4,5,6]
# 如何对items进行切片输出[2,3,4]
# （请用多种方法实现，一个方法2分）（6分）
# '''
# # items = [0,1,2,3,4,5,6]
# # print(items[2:5])
# # i = items[4:1:-1]
# # print(i[::-1])
# # list = []
# # for i in items:
# #     if i>1 and i<5:
# #         list.append(i)
# # print(list)

# # # 定义列表
# # nums = [1, 4, -5, 10, -7, 'N/A', 3, -1]

# # # 找出列表中小于0的数
# # negative_numbers = [num for num in nums if isinstance(num, (int, float)) and num < 0]

# # print(negative_numbers)



# '''
# 编写代码求以下列表中小于0的数
# nums = [1,4,-5,10,-7,'N/A',3,-1]（5分）
# '''
# nums = [1,4,-5,10,-7,'N/A',3,-1]
# for i in nums:
#     if isinstance(i,(int,float))and i<0:
#         print(i)


# '''编写一个对象，让其支持上下文管理协议（with语句）（10分）'''

# class Text():
#     def __enter__(self):
#         print('111')
#     def __exit__(self,exc_type,exc_val,exc_tb):
#         print('2222')
# with Text() as f:
#     print('333')



# '''冒泡排序'''
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# # 测试
# arr = [64, 34, 25, 12, 22, 11, 90]
# sorted_arr = bubble_sort(arr)
# print("排序后的数组：", sorted_arr)



# '''水仙花'''
# def is_narcissistic_number(num):
#     n = len(str(num))
#     temp = num
#     sum = 0
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** n
#         temp //= 10
#     return sum == num

# def find_narcissistic_numbers(start, end):
#     narcissistic_numbers = []
#     for i in range(start, end+1):
#         if is_narcissistic_number(i):
#             narcissistic_numbers.append(i)
#     return narcissistic_numbers

# # 测试
# start = 0
# end = 100
# narcissistic_numbers = find_narcissistic_numbers(start, end)
# print("在范围", start, "到", end, "内的水仙花数有：", narcissistic_numbers)



