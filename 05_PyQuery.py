from pyquery import PyQuery as pq 
from lxml import etree

html = '''<html>
    <head>
        <title>Hello PyQuery</title>
    </head>
    <body>
        <ul id="container">
            <li class="l1">l1</li>
            <li class="l2">l2</li>
            <li class="l3">l3</li>
        </ul>
    </body>
</html>'''

# doc = pq(etree.fromstring('<html><title>Hello PyQuery</title></html>'))
# doc = pq('http://www.baidu.com')
# print(doc)
# print(type(doc))


doc = pq(html)
# 设置起始位置
lis = doc('li:gt(-1)')
# 获取第一个 li
fli = doc('li:first-child')
# 获取最后一个 li
lli = doc('li:last-child')
# 获取指定 li
l2 = doc('li:nth-child(2)')
# 获取包含 last 的 li
cli = doc('li:contains("last")')
print(lis)
print(fli)
print(lli)
print(l2)
print(cli)

# ul = doc('#container')
# # 获取元素中的html
# # print(ul.html())
# li = doc('ul li')
# lis = li.items()
# ul_p= ul.parent()
# ul_c = ul.children()
# # print(ul_c)
# # print(ul_p)

# l2 = doc('ul .l2')
# l2_si = l2.siblings()
# # print(l2_si)
# #li2 = list(lis)==== [[<li.l1>], [<li.l2>], [<li.l3>]]

# #li2 = list(lis)[1]==== <li class="l2">l2</li>
# li2 = list(lis)[1]
# # print(li2)

# # 遍历
# lis = doc('ul li').items()
# # for i in lis:
# #     print(i)

