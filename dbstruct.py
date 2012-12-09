import pyodbc
from template import dbpath

dbfile = dbpath

def openDb():
    db = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb)};Dbq=%s' % dbfile )
    c = db.cursor()

    return (db,c)


