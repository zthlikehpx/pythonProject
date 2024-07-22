# from xml.etree import ElementTree as et
# import xml.dom.minidom as minidom

# root = et.Element('school')
# names = ['张三','李四']
# genders = ['男','女']
# ages = ['20','18']

# student1 = et.SubElement(root,'student')
# student2 = et.SubElement(root,'student')

# et.SubElement(student1,'name').text=names[0]
# et.SubElement(student1,'gender').text=genders[0]
# et.SubElement(student1,'age').text=ages[0]

# et.SubElement(student2,'name').text=names[1]
# et.SubElement(student2,'gender').text=genders[1]
# et.SubElement(student2,'age').text=ages[1]

# tree = et.ElementTree(root)
# rough_str = et.tostring(root,'utf-8')
# reparsed = minidom.parseString(rough_str)
# new_str = reparsed.toprettyxml(indent='\t')
# f = open('text.xml','w',encoding='utf-8')
# f.write(new_str)
# f.close()


import xml.etree.ElementTree as et
tree = et.parse('text.xml')

root = tree.getroot()
for i in root:
    print('name:',i[0].text, ',gender:',i[1].text, ',age:',i[2].text)