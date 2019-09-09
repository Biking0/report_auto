# 一次生成整月日报

import xlrd, xlwt


# 读取日报
day_book = xlrd.open_workbook('BD 河南省日健康巡检报告@20190901.xlsx')#打开一个excel

# 读取月报
month_book = xlrd.open_workbook('河南流量经营项目运维日报 V0.3 - 201908.xlsx')#打开一个excel
sheet = month_book.sheet_by_index(1)#根据顺序获取sheet

print(sheet.cell(4,2).value)
print(sheet.cell(4,3).value)


