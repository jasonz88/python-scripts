import sys, random
sys.path.append('C:\\Documents and Settings\\osr\\My Documents\\yohan\\SCRIPTS')
sys.path.append('c:\\Documents and Settings\\OSR\\My Documents\\yohan\\SCRIPTS\\webq')
#sys.path.append(os.getcwd())



import webq_result_util
from template import *

(db, c) = webq_result_util.initDbGetCursor()

for n in xrange(1, 10):
    cid = "TEST%d" % n
    c.execute("INSERT INTO login (cid,email,salu,name,account) VALUES ('%s', '%s', '%s', '%s', '%s')" % (cid,"kiddyq@gmail.com","Mr.","Zhang","OSR"))
for n in xrange(10, 20):
    cid = "TEST%d" % n
    c.execute("INSERT INTO login (cid,email,salu,name,account) VALUES ('%s', '%s', '%s', '%s', '%s')" % (cid,"survey@uts.cc.utexas.edu","Ms.","Inchauste","OSR"))
for n in xrange(20, 30):
    cid = "TEST%d" % n
    c.execute("INSERT INTO login (cid,email,salu,name,account) VALUES ('%s', '%s', '%s', '%s', '%s')" % (cid,"beth.vanriper@austin.utexas.edu","Ms.","Van Riper","OSR"))
for n in xrange(30, 40):
    cid = "TEST%d" % n
    c.execute("INSERT INTO login (cid,email,salu,name,account) VALUES ('%s', '%s', '%s', '%s', '%s')" % (cid,"provost@mail.utexas.edu","Mr.","Provost","OSR"))

db.commit()
db.close()

