import pyodbc
import generateLoginIDs
from excelDocument import ExcelDocument

def createCityEmailTable(xlsfile):
    doc = ExcelDocument(xlsfile)
    sheets = doc.sheets()
    s = doc.sheet(sheets[0])
    
    emails_per_city_table = {}
    
    #-- iterate over each row
    rowth = 0
    for eachEntry in s:
        rowth += 1
    
        #-- if first row, prepare the emails_per_city_table
        if ( rowth == 1 ):
            for city in eachEntry.keys():
                emails_per_city_table[city] = []
    
        #-- start collecting the e-mails
        for city in eachEntry.keys():
            email = eachEntry[city]
            if ( email == None ):
                continue
        
            email = email.strip()
            if ( email != '' ):
                emaillist = emails_per_city_table[city]
                emaillist.append(email)

    return emails_per_city_table

def prepareLoginTable(dbcur):
    try:
        dbcur.execute("""
          CREATE TABLE login
            ( cid varchar(16) PRIMARY KEY,
              email varchar(50),
              city varchar(50) )
          """)
    except:
        raise

                                      
def getLoginIDsPerCity(nthcity, cityname, emails ):
    #-- nthcity says the first city in the table, the second city, etc
    prefix = "%s%d" % (cityname[0:2], nthcity)
    rtnlist = []
    N = len(emails)
    generateLoginIDs.generateLoginIDs(prefix, N, rtnlist, 'ccddd')

    return rtnlist

def registerEachEmailEntryIntoLoginTable(dbcur, logins, emaillist, city):
    for (login, email) in zip(logins, emaillist):
        try:
            dbcur.execute( """
               INSERT INTO login (cid, email, city) VALUES ('%s', '%s', '%s')
               """ % ( login, email, city ) )
        except:
            raise

class CEntryCreator:
    def createObj(cols, value):
        obj = CEntry()
        obj.cols = cols
        obj.value = value
        return obj
    
    createObj = staticmethod(createObj)
    
class CEntry:
    cols = []
    value = []

    def __init__(self):
        self.cols = []
        self.isnumeric = []
        self.value = []

    def setData(colsarg, isnumericarg, valuearg):
        self.cols = colsarg
        self.value = valuearg
    
def registerEachEmailEntryIntoLoginTablePerEntryList(dbcur, entrylist):
    #-- entrylist contains list of CEntry object
    
    stringtype = 'abc'.__class__
    for eachentry in entrylist:
        valuelist = []
        for value in eachentry.value:
            if ( value.__class__ == stringtype ):
                valuelist.append("'%s'" % value)
            else:
                valuelist.append("%d" % value)

        sql_cmd = "INSERT INTO login (%s) VALUES (%s)" %  ( ','.join(eachentry.cols), ','.join(valuelist))
        
        try:
            dbcur.execute(sql_cmd)

        except:
            print "ERROR: at executing SQL: %s" % sql_cmd
            raise
        
            

def addTestLogins(dbcur):
    rtnlist = []
    generateLoginIDs.generateLoginIDs('TEST', 50, rtnlist)
    for login in rtnlist:
        dbcur.execute("""
           INSERT INTO login (cid) VALUES( '%s' )
           """ % ( login ) )
    

def initLoginTable(dbcur, emails_per_city_table):
    #-- prepare the login table
    prepareLoginTable(dbcur)

    nthcity = 0
    for eachcity in emails_per_city_table.keys():
        nthcity += 1
        emaillist = emails_per_city_table[eachcity]
        logins = getLoginIDsPerCity(nthcity, eachcity, emaillist )
        registerEachEmailEntryIntoLoginTable(dbcur, logins, emaillist, eachcity)
    addTestLogins(dbcur)
    
    
if ( __name__ == '__main__' ):
    dbfile = 'x:\\database\\casa.mdb'
    tablename = 'login'

    #-- open the database
    db = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};Dbq=%s' % dbfile )
    dbcur = db.cursor()

    #-- collect the email list per city in the dictionary format
    xlsfile = 'x:\\www\\casa\\SCRIPTS\\Volunteer Emails by City.xls'
    emails_per_city_table = createCityEmailTable(xlsfile)

    initLoginTable(dbcur, emails_per_city_table)
    
    db.commit()
    db.close()
