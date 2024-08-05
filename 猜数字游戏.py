import random
num = random.randint(0,30)
flag = False
print(num)
for i in range(1,6):
        ins = int(input('请输入数字：'))
        if num <ins:
            print('猜大了') 
        elif num > ins:
            print('猜小了')
        elif num == ins:
            flag = True
            print('猜对了')
            break
if flag:
    pass
else:
    print(f'5次机会用完了,答案是{num}')