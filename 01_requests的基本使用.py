# 导入模块
import requests

# 获取数据
response = requests.get('https://www.baidu.com')


# 解码
# response.encoding ='utf-8'
# print(response.text)
print(response.content.decode())