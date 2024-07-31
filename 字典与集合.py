d = {'name':'小米','age':17}
l = [('name', '小明'), ('age', 18)]
print(dict(l))
print(d['name'])
print(d.get('name'))
d['age'] = 36
print(d.get('age'))
# d.clear()
print(d)
print(len(d))
'''集合'''
s = {'a','b','c','a','a','a','b'}
s.remove('a')
print(s)