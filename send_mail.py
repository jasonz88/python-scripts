import sys, random
import mail_util
import time
import unicodedata
sys.path.append('C:\\Documents and Settings\\osr\\My Documents\\yohan\\SCRIPTS')
from excelDocument import ExcelDocument


sys.path.append('C:\\Documents and Settings\\osr\\My Documents\\yohan\\SCRIPTS')
sys.path.append('c:\\Documents and Settings\\OSR\\My Documents\\yohan\\SCRIPTS\\webq')
#sys.path.append(os.getcwd())

from excelDocument import ExcelDocument

import webq_result_util
from template import *



'''

if __name__ == "__main__":
    mail_server = mail_util.login("or2553","utosr!986")
    mail_content_base = open("mail_content.txt", "r").read()

    xlsfile = "cidandemail.xls"

    doc = ExcelDocument(xlsfile)
    sheets = doc.sheets()
    s = doc.sheet(sheets[0])

    n_total = 0
   
    for eachEntry in s:
        cid = unicodedata.normalize('NFKD', eachEntry['cid']).encode('ascii','ignore')
        email = unicodedata.normalize('NFKD', eachEntry['Email']).encode('ascii','ignore')
            
        mail_content = mail_content_base.replace("userid", "%s"%cid)
        n_total += 1
        mail_util.send_mail(mail_server,"Office of Survey Research<osr@austin.utexas.edu>",email,"Use and Satisfaction Survey of Technology Equipped Classrooms",mail_content,"")
        print "Done mailing... %s %s"%(cid, email)
        time.sleep(0.1)
        
    mail_util.logout(mail_server)
    print "total: ",n_total
'''
if __name__ == "__main__":
    (db, c) = webq_result_util.initDbGetCursor()
    mail_server = mail_util.login("or2553","utosr!986")
    mail_content_base = open("mail_content.txt", "r").read()

    #c.execute("SELECT * FROM login WHERE cid not like 'TEST%%' and cid not like 'vTEST%%' and cid not like 'bTEST%%' and cid not in (select cid from result where lastnode = '11' or lastnode = '10')")
    c.execute("SELECT * FROM login WHERE cid not like 'TEST%'")
    mailing_list = c.fetchall()
    
    #print mailing_list, len(mailing_list)
    #sys.exit(0)
    
    for mailing_element in mailing_list:
        cid = mailing_element[0]
        name = mailing_element[1]
        salu=mailing_element[3]
        email=mailing_element[4]
        
        
        if email == "EMPTY":
            continue
            
        print cid, email

        mail_content = mail_content_base.replace("userid", cid)
        mail_content = mail_content.replace("Mr./Ms.",salu+" "+name)
        
        #mail_util.send_mail(mail_server, "Office of Survey Research<osr@austin.utexas.edu>",email,"Real Time Location Services Survey", mail_content, "")
        print "Done mailing... %s %s"%(cid, email)
        
    mail_util.logout(mail_server)
print mail_content
