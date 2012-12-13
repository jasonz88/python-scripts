import sys, random
sys.path.append('C:\\Documents and Settings\\osr\\My Documents\\yohan\\SCRIPTS')
sys.path.append('c:\\Documents and Settings\\OSR\\My Documents\\yohan\\SCRIPTS\\webq')
#sys.path.append(os.getcwd())

from excelDocument import ExcelDocument

import webq_result_util
from template import *

(db, c) = webq_result_util.initDbGetCursor()
xlsfile = "Hospital Tech Email List-Sample 12-12-12.xls"

c.execute("SELECT email FROM login WHERE cid not like 'TEST%'")
emaillist=c.fetchall()

doc = ExcelDocument(xlsfile)
sheets = doc.sheets()
s = doc.sheet(sheets[0])

n_missing = 0
n_total = 0
count = 1000
for eachEntry in s:
    #last = eachEntry['LastName']
    #first = eachEntry['FirstName']
    email = eachEntry['Email']
    firstname=eachEntry['First Name']
    lastname=eachEntry['Last Name']
    name=firstname+" "+lastname
    email=email.replace("'", "''")
    name=name.replace("'", "''")
    phone=eachEntry['Phone']
    company=eachEntry['Company']
    company=company.replace("'", "''")
    state=eachEntry['State']
    timezone=eachEntry['Time Zone']
    cid = "ST%d"%count
    count +=1
    #if email in emaillist:
        #print email
    #else:
        #print "INSERT INTO login (cid,email,phone,accname,name,state,timezone) VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (cid,email,phone,company,name,state,timezone)
        #c.execute("INSERT INTO login (cid,email,phone,accname,name,state,timezone) VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (cid,email,phone,company,name,state,timezone))
    #c.execute("INSERT INTO login (cid,email,phone,accname,name,state,timezone) SELECT '%s','%s','%s','%s','%s','%s','%s' FROM login WHERE NOT EXISTS (SELECT * FROM login WHERE email='%s')" % (cid,email,phone,company,name,state,timezone,email))
    n_total += 1
    

print "n_total = %d" % n_total
print "n_missing = %d" % n_missing

db.commit()
db.close()
