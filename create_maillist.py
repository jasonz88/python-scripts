import pyodbc
import dbstruct

(db,c) = dbstruct.openDb()
c.execute("SELECT * FROM login")

fh = open('maillist.txt', 'w')

rows = c.fetchall()
for row in rows:
    first = getattr(row, 'firstname')
    last = getattr(row, 'lastname')
    email = getattr(row, 'email')
    cid = getattr(row, 'cid')

    if ( email == None ):
        print "SKIPPED MISSING EMAIL: %s %s [%s]" % (first,last,cid)
        continue
        
    if ( cid[0:4] == 'TEST' ):
        continue
    
    fh.write('"%s %s [%s]" <%s>, ' % (first,last,cid,email))

fh.close()

    
