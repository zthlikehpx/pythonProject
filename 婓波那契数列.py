def chicken_and_rabbit(a, b):
    for x in range(a + 1):
        y = a - x
        if 2 * x + 4 * y == b:
            return x, y
    return None
 
# 输入头数
a=10;
#输入脚数
b=20;
result = chicken_and_rabbit(a, b)
if result:
    print("鸡的数量为：", result[0], "兔子的数量为：", result[1])
else:
    print("无解")