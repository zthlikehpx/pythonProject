# 学过的同学先做一下这个练习，网上有答案，先自己做
# 习题1：
# -直接在控制台使用命令行运行
# -程序运行之后倒计时1分钟之后结束
# -随机出100以内的2个整数加减乘除运算题目（除法确保能够除尽，但除数不能为0）
# -每出一道题目，由玩家给出答案，然后程序判断对错，接着出下一题，并且显示剩余时间
# -1分钟时间结束，显示总题数和正确率（正确率精确到小数点后2位），并将之前的题目和答案显示出来




import random
import time

def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operations = ['+', '-', '*', '/']
    operation = random.choice(operations)

    # 确保除法能够整除，但除数不能为0
    if operation == '/':
        while num1 % num2 != 0:
            num2 = random.randint(1, 100)
        question = f"{num1} {operation} {num2}"
        answer = eval(question)
    else:
        question = f"{num1} {operation} {num2}"
        answer = eval(question)
    return question, answer

def quiz():
    start_time = time.time()
    end_time = start_time + 60  # 设置1分钟倒计时
    correct_answers = 0
    total_questions = 0
    questions_answers = []

    while time.time() < end_time:
        question, answer = generate_question()
        print(f"题目：{question} = ", end="")
        try:
            user_answer = float(input())
            if user_answer == answer:
                print("正确！")
                correct_answers += 1
            else:
                print(f"错误！正确答案是 {answer}")
            total_questions += 1
            questions_answers.append((question, answer, user_answer))
            remaining_time = int(end_time - time.time())
            print(f"剩余时间：{remaining_time} 秒\n")
        except ValueError:
            print("请输入一个有效的数字！")
            print(f"剩余时间：{remaining_time} 秒\n")
            
        if time.time()==end_time:
            break
    # 显示结果
    print(f"总题数：{total_questions}")
    if total_questions > 0:
        accuracy = (correct_answers / total_questions) * 100
    else:
        accuracy = 0
    print(f"正确率：{accuracy:.2f}%")
    for q, a, ua in questions_answers:
        print(f"题目：{q} = {a}, 您的答案：{ua}")

# 运行测验
quiz()
