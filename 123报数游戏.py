def cal(que):
    num = 0
    while len(que)>1:
        qu = que[:]
        for i in qu:
            num +=1
            print(f'当前{i},报数{num}')
            if num ==3:
                que.remove(i)
                num=0
    else:
        print(f'当前{que}胜利')
while True:
    ins = input('输入游戏总人数：')
    if ins.isdigit():
        num = int(ins)
        que = [i+1 for i in range(num)]
        print(que)
        cal(que)
    elif ins =='q':
        break
    else:
        print('输入错误')