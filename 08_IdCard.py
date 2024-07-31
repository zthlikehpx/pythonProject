# 课后任务：
# 1.读取身份证信息表
# 2.用正则匹配出生日期
import re
# try:
#     with open('C:/Users/admin/Desktop/身份证信息.csv','r',encoding='utf-8')as f:
#         id = f.read()
#         birthday = re.findall(r'出生日期:(.+?),性别',id)
#         with open('C:/Users/admin/Desktop/birthday.txt','w',encoding='utf-8')as fs:
#             for a in birthday:
#                 fs.write(a+'\n')
# except FileNotFoundError:
#     print('文件不存在or文件路径不正确')


read = 'C:/Users/admin/Desktop/身份证信息.csv'
write = 'C:/Users/admin/Desktop/birthday.txt'

def rw(read,write):
    try:
        with open(read,'r',encoding='utf-8')as f:
            id = f.read()
    except UnicodeDecodeError:
        with open(read,'r',encoding='gbk')as f:
            id = f.read()
    except FileNotFoundError:
        print('文件不存在or文件路径不正确')


    birthday = re.findall(r'出生日期:(.+?),性别',id)
    try:
        with open(write,'w',encoding='utf-8')as f:
            for a in birthday:
                f.write(a+'\n')
    except UnicodeDecodeError:
         with open(write,'w',encoding='gbk')as f:
            for a in birthday:
                f.write(a+'\n')

rw(read,write)