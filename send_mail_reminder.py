import mail_util
import sys
sys.path.append('C:\\Documents and Settings\\osr\\My Documents\\yohan\\SCRIPTS')
from excelDocument import ExcelDocument

import dbstruct

if __name__ == "__main__":
    mail_server = mail_util.login("or2553","utosr!986")
    mail_content_base = open("mail_content_reminder1.txt", "r").read()

    (db,c) = dbstruct.openDb()
    c.execute("SELECT * FROM login WHERE cid not like 'TEST%%' and cid not like 'vTEST%%' and cid not like 'bTEST%%' and cid not like 'otest%%' and cid not in (select cid from result where lastnode = '11' or lastnode = '10')")
    #c.execute("SELECT * FROM login WHERE cid like 'btest%' or cid like 'vtest%' or cid like 'otest%'")
    #c.execute("SELECT * FROM login WHERE cid like 'Test31'")
    mailing_list = c.fetchall()
    
    #print mailing_list, len(mailing_list)
    #sys.exit(0)
    
    for mailing_element in mailing_list:
        cid = mailing_element[0]
        to_id = mailing_element[3]
        
        if to_id == "EMPTY":
            continue
            
        print cid, to_id

        mail_content = mail_content_base.replace("USERID", cid);
        
        mail_util.send_mail(mail_server, "Office of Survey Research<osr@austin.utexas.edu>",to_id,"Killeen ISD Climate Survey", mail_content, "")
        print "Done mailing... %s %s"%(cid, to_id)
        
    mail_util.logout(mail_server)
