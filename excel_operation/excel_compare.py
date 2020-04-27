import xlrd
#Reading two Excel Sheets ztest.xlsx 
path1 = (r"C:\Users\kk186085\OneDrive - Teradata\My Learnings\Python Prog\excel_operation\ztest.xlsx")
path2 = (r"C:\Users\kk186085\OneDrive - Teradata\My Learnings\Python Prog\excel_operation\kapil_sheet2.xlsx")
input_excel1 = xlrd.open_workbook(path1)
input_excel2 = xlrd.open_workbook(path2)
input_sheet1 = input_excel1.sheet_by_index(0) # sheet here is next page sheet in excel
input_sheet2 = input_excel2.sheet_by_index(0)
print(input_sheet2.nrows)

# # print(input_sheet1.nrows)
# # print(input_sheet1.ncols)
# # print(input_sheet1.cell_value(1,4)) # (row,col)
# names = []
# date = []
# #names.append(input_sheet1.cell_value(2,0))
# # names.append(input_sheet1.cell_value(2,0))
# # names.append(input_sheet1.cell_value(3,0))
# # print(names)
# # list(set(a).intersection(set(b)))
# # for y in range(input_sheet1.nrows):
# #     names.append(input_sheet1.cell_value(y,0))

# if input_sheet1.cell_value(1,4) == input_sheet1.cell_value(2,4):
#     print ("equal")
# else:
#     print ("unequal")