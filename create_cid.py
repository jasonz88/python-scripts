import sys
sys.path.append('C:\\Documents and Settings\\osr\\My Documents\\yohan\\SCRIPTS')
from excelDocument import ExcelDocument
import xlwt

wbk = xlwt.Workbook()
sheet = wbk.add_sheet('datasheet')



xlsfile = "RTLS Call Survey List 08-26-12.xls"
maillist = open("maillist.txt", "w")

doc = ExcelDocument(xlsfile)
sheets = doc.sheets()
s = doc.sheet(sheets[0])


n_missing = 0
n_total = 0
count = 1000
row=1

maillist_data = ""
sheet.write(0,0,"cid")
sheet.write(0,1,"Email")
sheet.write(0,2,"Name")
sheet.write(0,3,"AccName")
sheet.write(0,4,"Salutation")
sheet.write(0,5,"Phone")
"""for i in range(1,3):
    sheet.write(i,0,"TEST%d" % i)
    sheet.write(i,1,"kiddyq@gmail.com")
"""
for eachEntry in s:
    #last = eachEntry['Last Name']
    #first = eachEntry['First Name']
    #print eachEntry
    accname=eachEntry['Hospital Contact List']
    email = eachEntry['RTLS project']
    name=eachEntry['RTLS - Environmental Monitoring & Asset Location Project']
    sex=eachEntry['F3']
    phone=eachEntry['F5']
    
    #if first == None or last == None:
    #    break

    #firststr = first.replace("'", "''")
    #laststr = last.replace("'", "''")

    if ( email == None or email == '' ):
        #print "MISSING EMAIL: %s" % (accname)
        n_missing += 1
    else:
        emailstr = "%s" % email
        accnamestr="%s" % accname
        namestr="%s" % name
        salutation="Ms." if sex=="f" else "Mr."
        cid = "CT%d"%count
        phonestr="%s" % phone
        sheet.write(row,0,cid)
        sheet.write(row,1,emailstr)
        sheet.write(row,2,namestr)
        sheet.write(row,3,accnamestr)
        sheet.write(row,4,salutation)
        sheet.write(row,5,phonestr)
        maillist_data = maillist_data + "%s|%s|%s|%s|%s|%s\n"%(cid,emailstr,namestr,accnamestr,salutation,phonestr)
        count += 1

    n_total += 1
    row+=1

maillist.write(maillist_data)
maillist.close()
wbk.save('cidandemail.xls')
print "n_total = %d" % n_total
print "n_missing = %d" % n_missing
