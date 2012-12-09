import pyodbc
import dbstruct
import unicodedata
import sys
import time
from dontsend_list_2012 import dontsend_list

(db,c) = dbstruct.openDb()
c.execute("SELECT * FROM login")

import mail_util

if __name__ == "__main__":
    mail_server = mail_util.login("or2553","utosr!986")
    mail_content_base = open("mail_content_followup_final.txt", "r").read()
    
    rows = c.fetchall()
    
    c.execute("SELECT * FROM result")
    results = c.fetchall()
    results_cids = [unicodedata.normalize('NFKD', r[0]).encode('ascii','ignore')
                        for r in results]
    results_steps = [int(r[-1]) for r in results]
    
    num_completed = 0
    num_unfinished = 0
    num_notstarted = 0
    num_emailsent = 0
    num_total = 0
    
    for row in rows:
        
        cid = unicodedata.normalize('NFKD', row[0]).encode('ascii','ignore')
        #first = unicodedata.normalize('NFKD', row[1]).encode('ascii','ignore')
        #last = unicodedata.normalize('NFKD', row[2]).encode('ascii','ignore')
        email = unicodedata.normalize('NFKD', row[3]).encode('ascii','ignore')
        
        '''
        cid = getattr(row, 'cid')
        first = getattr(row, 'firstname')
        last = getattr(row, 'lastname')
        email = getattr(row, 'email')
        '''
        if ( email in dontsend_list ):
            print "SKIPPED [DONTSEND]: ", email
            continue
        
        
        
        if ( cid[0:4] == 'TEST' ):
            #pass
            continue
        
        send_mail = False
        index = None
        try: index = results_cids.index(cid)
        except: pass
        
        if not index:
            send_mail = True
            #print "CID", cid, "has not started."
            num_notstarted += 1
        elif index and results_steps[index] < 8:
            send_mail = True
            #print "CID", cid, "started but did not finish survey."
            num_unfinished += 1
        else:
            #print "CID", cid, "finished survey."
            num_completed += 1
        
        
        num_total += 1
        if send_mail:
            num_emailsent += 1
            mail_content = mail_content_base.replace("userid", cid)
            
            
            
            '''mail_util.send_mail(mail_server,
                "Office of Survey Research<osr@austin.utexas.edu>",
                email,
                "Use and Satisfaction Survey of Technology Equipped Classrooms",
                mail_content,
                [])'''
            print "Done mailing... [%s] %s"%(cid, email)
        
    print "All mail sent (%d total)." % num_emailsent
    print "Completed:\t%d\t(%%%.4f)" % (num_completed, (float(num_completed) / num_total))
    print "Unfinished:\t%d\t(%%%.4f)" % (num_unfinished, (float(num_unfinished) / num_total))
    print "Not started:\t%d\t(%%%.4f)" % (num_notstarted, (float(num_notstarted) / num_total))
    print "Num Persons in survey:", num_total
    
    mail_util.logout(mail_server)
