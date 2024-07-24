# from docx import Document
# document = Document()
# t0 = document.add_heading('标题0', 0)
# document.add_heading('标题1', 1)
# document.add_heading('标题2', 2)

# table =document.add_table(rows=4,cols=3,style='Table Grid')
# # rows---行
# # cols---列
# hc = table.rows[0].cells
# hc[0].text = '姓名'
# hc[1].text = '年龄'
# hc[2].text = '地址'


# bc1 = table.rows[1].cells
# bc1[0].text = '张三'
# bc1[1].text = '22'
# bc1[2].text = '广东省'

# bc2 = table.rows[2].cells
# bc2[0].text = '李四'
# bc2[1].text = '33'
# bc2[2].text = '重庆市'

# bc3 = table.rows[3].cells
# bc3[0].text = '李无'
# bc3[1].text = '33'
# bc3[2].text = '湖南省'
# document.save('C:/Users/admin/Desktop/test.docx')


# document = Document('C:/Users/admin/Desktop/test.docx')
# ps = [i.text for i in document.paragraphs]
# for a in ps:
#     print(a)

# ts =[b for b in document.tables]
# for t in ts:
#     for row in t.rows:
#         for cell in row.cells:
#             print(cell.text,end=' ')
#         print()