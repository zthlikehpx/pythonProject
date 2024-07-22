from bs4 import BeautifulSoup

# soup = BeautifulSoup('<html>data</html>','lxml')
# print(soup)

s = """<div>
<p>岗位职责:</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<P>必备要求:</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p id="link2">技术要求:</p>
<p>1、一年以上 Python开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉NVC、MVVM等概念以及相关wEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握SQL，熟练使用 MySQL/PostgresQL中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/cSS/HTML5，JQuery,React.Vue.js</p>
<p>&nbsp;<br></p>
<p id="link1">加分项:</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>
</div>"""


# find 查找第一个标签
# findAll 查找所有标签
soup1 = BeautifulSoup(s,'lxml')
title = soup1.find(id="link1")
print(title)

# attrs 属性字典
title1 = soup1.find(attrs={'id':'link1'})
print(title1)

# 根据文本查找内容
title2 = soup1.find(text="技术要求:")
print(title2)

print(type(title2))
print(title2.name)
