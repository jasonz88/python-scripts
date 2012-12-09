import sys
sys.path.append('C:\\Documents and Settings\\osr\\My Documents\\yohan\\SCRIPTS\\webq')

import webq_result_util
from template import *

from dontsend_list import dontsend_list

import dbstruct
(db,c) = dbstruct.openDb()

#- get last page
lastpage = webq_result_util.getLastPage(c)

#- get the ones that have not finished or have not touched the survey
sql_cmd = """
SELECT
  l.cid,l.firstname,l.lastname,l.email,r.lastnode
FROM
  login l LEFT OUTER JOIN result r ON r.cid=l.cid
WHERE
  l.name NOT LIKE 'TEST%%'
  AND (r.lastnode is NULL OR r.lastnode <> '%d')
""" % (lastpage)
sql_cmd = """
SELECT
  l.cid,l.firstname,l.lastname,l.email,r.lastnode
FROM
  login l LEFT OUTER JOIN result r ON r.cid=l.cid
WHERE
  (l.firstname NOT LIKE 'TEST%%' ) AND (r.lastnode is NULL OR r.lastnode <> '8')
""" 
print sql_cmd 
c.execute(sql_cmd)

#- iterate over the list
counter = 0
fh = open('maillist_reminder.txt', 'w')
for eachrow in c.fetchall():
    cid      = webq_result_util.getRowAttr(eachrow,'cid')
    firstname     = webq_result_util.getRowAttr(eachrow,'firstname')
    lastname     = webq_result_util.getRowAttr(eachrow,'lastname')
    name = '%s %s' % ( firstname, lastname )
    email    = webq_result_util.getRowAttr(eachrow,'email')
    lastnode = webq_result_util.getRowAttr(eachrow,'lastnode')

    if ( email in dontsend_list ):
        print "SKIPPED [DONTSEND]: ", email
        continue

    fh.write('"%s [%s]" <%s>, ' % (name,cid,email))
    print('"%s [%s]" <%s> (%s) ' % (name,cid,email,lastnode))
    counter += 1    

fh.close()

print "TOTAL FIRST REMINDER SAMPLE = ", counter

    
