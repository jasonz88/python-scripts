import sys, random
sys.path.append('C:\\Documents and Settings\\osr\\My Documents\\yohan\\SCRIPTS')
from excelDocument import ExcelDocument

import dbstruct

files = ["Category_A.csv","Category_B.csv", "Category_C.csv"]
(db,c) = dbstruct.openDb()
c.execute("CREATE TABLE login (cid varchar(16) PRIMARY KEY, vipid varchar(100), email varchar(100), category varchar(6)")

for file in files:
    xlsfile = open(file)
    print xlsfile

    for line in xlsfile:
        words = line.split(',')
        print words
        caseid = words[0]
        vipid = words[1].rstrip('\n')
        email = words[2].rstrip('\n')
        category = words[3].rstrip('

        print "%s %s" % (caseid, password)
        
        c.execute("INSERT INTO login (cid,password) VALUES ('%s', '%s')" % (caseid,password))


db.commit()
db.close()
