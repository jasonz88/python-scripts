import sys, random
sys.path.append('C:\\Documents and Settings\\osr\\My Documents\\yohan\\SCRIPTS')
sys.path.append('c:\\Documents and Settings\\OSR\\My Documents\\yohan\\SCRIPTS\\webq')
#sys.path.append(os.getcwd())

from excelDocument import ExcelDocument

import webq_result_util
from template import *

(db, c) = webq_result_util.initDbGetCursor()
xlsfile = "cidandemail.xls"

doc = ExcelDocument(xlsfile)
sheets = doc.sheets()
s = doc.sheet(sheets[0])

n_missing = 0
n_total = 0
for eachEntry in s:
    #last = eachEntry['LastName']
    #first = eachEntry['FirstName']
    email = eachEntry['Email']
    name=eachEntry['Name']
    phone=eachEntry['Phone']
    #if first == None or last == None:
     #   break

    #firststr = first.replace("'", "''")
    #laststr = last.replace("'", "''")

    """if ( email == None or email == '' ):
        print "MISSING EMAIL: %s %s [%s]" % (first,last,eid)
        emailstr = "NULL"
        n_missing += 1
    else:"""
    #emailstr = "'%s'" % email

    #print "('%s', '%s', '%s', %s)\n"% (eid,firststr,laststr,emailstr)
    c.execute("UPDATE login SET phone='%s' WHERE name ='%s'" % (phone,name))
    n_total += 1

print "n_total = %d" % n_total
print "n_missing = %d" % n_missing

db.commit()
db.close()
