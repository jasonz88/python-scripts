import sys, random
sys.path.append('C:\\Documents and Settings\\osr\\My Documents\\yohan\\SCRIPTS')

import dbstruct

(db,c) = dbstruct.openDb()

nn=130


for cid in range(nn, nn+10):
    c.execute("INSERT INTO login (cid,campus,name,email,title) VALUES ('vtest%d', 'UT', 'Name', 'survey@uts.cc.utexas.edu', 'student')" % (cid))


for cid in range(nn+10, nn+20):
    c.execute("INSERT INTO login (cid,campus,name,email,title) VALUES ('btest%d', 'UT', 'Name', 'beth.vanriper@austin.utexas.edu', 'student')" % (cid))

for cid in range(nn+20, nn+30):
    c.execute("INSERT INTO login (cid,campus,name,email,title) VALUES ('otest%d', 'UT', 'Name', 'provost@mail.utexas.edu', 'student')" % (cid))

db.commit()
db.close()