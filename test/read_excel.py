import xlrd
#只能读不能写
# book = xlrd.open_workbook('stu.xls')#打开一个excel
book = xlrd.open_workbook('stu_1.xls')#打开一个excel
sheet = book.sheet_by_index(0)#根据顺序获取sheet
sheet2 = book.sheet_by_name('case1_sheet')#根据sheet页名字获取sheet
# print(sheet.cell(0,0).value)#指定行和列获取数据

print(sheet.cell(0,0).value,sheet.cell(0,1).value,sheet.cell(0,2).value,sheet.cell(0,3).value)#指定行和列获取数据

print(sheet.cell(0,1).value)
print(sheet.cell(0,2).value)
print(sheet.cell(0,3).value)
print(sheet.ncols)#获取excel里面有多少列
print(sheet.nrows)#获取excel里面有多少行
print(sheet.get_rows())#
for i in sheet.get_rows():
    print(i)#获取每一行的数据
print(sheet.row_values(0))#获取第一行
for i in range(sheet.nrows):#0 1 2 3 4 5
    print(sheet.row_values(i))#获取第几行的数据

print(sheet.col_values(1))#取第一列的数据
for i in range(sheet.ncols):
    print(sheet.col_values(i))#获取第几列的数据