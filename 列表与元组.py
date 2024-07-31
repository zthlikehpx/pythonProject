l = [1024,0.5,'python']
print(l[1])  #0.5
print(l[1:])  #[0.5, 'python']

del(l[1])

l = ['d', 'b', 'a', 'f', 'd','a','b','f','f','f']
c = {}
for i in l:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
sorted_c = sorted(c.items(), key=lambda x: x[1], reverse=True)
print(sorted_c)
top_three = sorted_c[:2]
for item in top_three:
    print(f"{item[0]} 出现了 {item[1]} 次")

'''元组'''
t = (1024,0.5,'python')
print(t[0])
print(t[0:])
print(len(t))

print(tuple(l))