import random
def mp(l):
    '''正序'''
    for i in range(0,len(l)):
        for j in range(0,len(l)-1-i):
            if l[j]>l[j+1]:
                tmp = l[j]
                l[j] = l[j+1]
                l[j+1] = tmp
    print(l)


def mp_r(l):
    '''逆序'''
    for i in range(0,len(l)):
        for j in range(0,len(l)-1-i):
            if l[j]<l[j+1]:
                tmp = l[j]
                l[j] = l[j+1]
                l[j+1] = tmp
    print(l)

while True:
    ins = input('请输入乱序列表的个数(q退出)：')
    if ins.isdigit():
        num = int(ins)
        l = [random.randint(0,30) for _ in range(num)]
        print('乱序列表为：',l)
        mp(l)
        mp_r(l)
    elif ins =='q':
        break
    else:
        print('111')