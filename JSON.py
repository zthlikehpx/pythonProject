import json

d = {'id':'001', 'name':'张三', 'age':'20'}
# 有中文====ensure_ascii=False
j = json.dumps(d, ensure_ascii=False)
print(j)


import json
# dumps 可以对数据格式化
# dump 可以将python对象转换成json文件
d = {'id':'001', 'name':'张三', 'age':'20'}
j = json.dumps(d, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
print(j)

# ensure_ascii=False: 允许输出非ASCII字符，这里是为了确保中文字符可以正常显示。
# sort_keys=True: 对字典的键进行排序，使得输出的JSON字符串键是有序的。
# indent=4: 输出的JSON字符串具有4个空格的缩进，使得格式更加清晰。
# separators=(',', ': '): 定义了分隔符，逗号后面不加空格，而冒号后面加一个空格，也是为了格式化输出。


import json

d = {'id':'001', 'name':'张三', 'age':'20'}
with open('test.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=4, ensure_ascii=False)


# loads()可将json格式转换成python对象
import json
j =  '{"id":"001", "name":"张三", "age":"20"}'
d = json.loads(j)
print(d)

# load() 将文件对象转换成python对象
with open('test.json',encoding='utf-8') as f:
    print(json.load(f))