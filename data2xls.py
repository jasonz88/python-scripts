import xlwt
import sys


wbk = xlwt.Workbook()
sheet = wbk.add_sheet('datasheet')
 
row = 0
f = open(sys.argv[1],'r')

for line in f:
    L = line.rstrip().split('|')
    if L[0]=="":
        continue
    for i in range(len(L)):
        sheet.write(row,i,L[i])
    row += 1
 
wbk.save('reformatted.data.xls')