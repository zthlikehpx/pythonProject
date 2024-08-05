'''兔子四只腿，鸡两只腿'''
def animal(head:int,leg:int):
    rabbit = (leg - head *2)//2
    chicken = head - rabbit
    tmp = 4*rabbit+2*chicken
    if tmp ==leg_num and rabbit>=0 and chicken >=0:
        return True,chicken,rabbit
    else:
        return False,0,0

while True:
    print('鸡兔同笼处理程序')

    while True:
        head_str = input('输入头的数量：')
        if head_str.isdigit():
            head_num =int(head_str)
            break
        else:
            print('数据异常，请重新输入')
    while True:
        leg_str = input('输入腿的数量：')
        if leg_str.isdigit():
            leg_num =int(leg_str)
            break
        else:
            print('数据异常，请重新输入')

    if head_num>leg_num:
        print('数据输入错误，重新输入')
    else:
        status,chicken,rabbit = animal(head_num,leg_num)
        if status:
            print(f'{head_num}个头{leg_num}条腿，{rabbit}只兔子{chicken}只鸡')