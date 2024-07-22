import xlwt
wb = xlwt.Workbook()
sh = wb.add_sheet('test')
font = xlwt.Font()
font.bold = True
alm = xlwt.Alignment()
alm.horz = xlwt.Alignment.HORZ_CENTER
# xlwt.Alignment.HORZ_CENTER 居中对齐
# alm.horz = 0x01 左对齐
style1 = xlwt.XFStyle()
style2 = xlwt.XFStyle()
style1.font = font
style2.alignment = alm


sh.write(0, 1, '姓名', style1)
sh.write(0, 2, '年龄', style1)
sh.write(1, 1, '张三')
sh.write(1, 2, 50, style2)
sh.write(2, 1, '李四')
sh.write(2, 2, 30, style2)
sh.write(3, 1, '王五')
sh.write(3, 2, 40, style2)
sh.write(4, 1, '赵六')
sh.write(4, 2, 60, style2)

wb.save('C:/Users/admin/Desktop/test2.xls')


import xlsxwriter
workbook = xlsxwriter.Workbook('C:/Users/admin/Desktop/test4.xlsx')
sh = workbook.add_worksheet('test')
fmt1 = workbook.add_format()
fmt2 = workbook.add_format()

fmt1.set_bold(True)
fmt1.set_align('center')
fmt2.set_align('center')

# 数据
data = [
    ['姓名', '年龄'],
    ['张三', 50],
    ['李四', 30],
    ['王五', 40],
    ['赵六', 60],
]
sh.write_row('A1', data[0], fmt1)
sh.write_row('A2', data[1], fmt2)
sh.write_row('A3', data[2], fmt2)
sh.write_row('A4', data[3], fmt2)
sh.write_row('A5', data[4], fmt2)
chart = workbook.add_chart({'type': 'line'})
# 创建图表
chart.add_series(
    {
        'name':'=test!$A$1',
        # x轴
        'categories':'=test!$A$2:$A$5',
        # y轴
        'values':   '=test!$B$2:$B$5'
    }
)
chart.set_title({'name':'用户年龄折线图'})
chart.set_x_axis({'name':'姓名'})
chart.set_y_axis({'name':'年龄'})
sh.insert_chart('A10', chart)
workbook.close()



# 读取
import xlrd

# xlrd库主要支持旧版本的.xls格式
# wb = xlrd.open_workbook('C:/Users/admin/Desktop/test4.xlsx')
wb = xlrd.open_workbook('C:/Users/admin/Desktop/test2.xls')
print(wb.sheet_names())
print(wb.nsheets)
