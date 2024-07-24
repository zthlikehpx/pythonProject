# 课后任务：
# 1.读取身份证信息表
# 2.用正则匹配出生日期
import re
try:
    with open('C:/Users/admin/Desktop/身份证信息.csv','r',encoding='utf-8')as f:
        id = f.read()
        birthday = re.findall(r'出生日期:(.+?),性别',id)
        with open('C:/Users/admin/Desktop/birthday.text','w',encoding='utf-8')as fs:
            for a in birthday:
                fs.write(a+'\n')
except FileNotFoundError:
    print('文件不存在or文件路径不正确')


    