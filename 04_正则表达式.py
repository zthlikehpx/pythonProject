import re
# rs = re.findall('abc','adcabcdssdssd')
# rs = re.findall('a.c','adcabcdssdssd')
rs = re.findall('a[bc]c','adcabcdssdssd')
# \  转义符
# rs = re.findall('a\.c','a.c')
# print(rs)


# re.findall(string: str, flags:)
# flags ---- 匹配模式
rs = re.findall('a.bc','a\nbc',re.DOTALL)
# print(rs)


# 分组--() --- 返回与括号中匹配的内容，小括号两边则是定位
rs = re.findall('a(.+)bc','a\nbc',re.DOTALL)
print(rs)


# r原串---消除正则对转义符的影响
rs = re.findall(r'a\\nbc','a\\nbc')
print(rs)