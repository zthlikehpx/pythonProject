'''函数递归'''
def get_drink(money,drink,bottle,cap):
    if money>0:
        drink +=money
        bottle +=money
        cap +=money
        money = 0
        print(f'花钱购买了{drink}瓶，当前剩余{money}元，瓶子剩余{bottle}个，瓶盖有{cap}个')
    elif bottle >=2:
        tmp = bottle//2
        bottle =bottle%2
        bottle+=tmp
        cap += tmp
        drink +=tmp
        print(f'花钱购买了{drink}瓶，当前剩余{money}元，瓶子剩余{bottle}个，瓶盖有{cap}个')
    elif cap >=3:
        tmp = cap//3
        cap =cap%3
        cap += tmp
        bottle +=tmp
        drink +=tmp
        print(f'花钱购买了{drink}瓶，当前剩余{money}元，瓶子剩余{bottle}个，瓶盖有{cap}个')
    if bottle>=2 or cap>=3:
        get_drink(money,drink,bottle,cap)


while True:
    ins = input('请输入数值：')
    if ins.isdigit():
        money = int(ins)
        drink = 0
        cap = 0
        bottle =0
        get_drink(money,drink,bottle,cap)
    else:
        print('错误，重新输入')
money =20
drink =0
cap = 0
bottle =0
get_drink(money,drink,bottle,cap)