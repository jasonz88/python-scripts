import sys
import dbstruct
import unicodedata

(db,c) = dbstruct.openDb()
c.execute("SELECT TOP 1 * FROM result_stats")

rows = c.fetchall()

for row in rows:
    lastpage = int(unicodedata.normalize('NFKD', row[1]).encode('ascii','ignore'))

desc = []
data = []


for pagei in range(1, lastpage):
    c.execute("SELECT TOP 1 * FROM result_page_%d" % pagei)
    
    if pagei == 1:
        desc.append(c.description[0][0])
        desc.append('|')
    
    for coli in range(3, len(c.description)):
        desc.append(c.description[coli][0])
        desc.append('|')
  

#c.execute("SELECT cid FROM result where cid not like '%test%'")
c.execute("SELECT cid FROM result WHERE lastnode > '1' and cid not like '%TES'")
cids = c.fetchall()

for cid in cids:
    cid = unicodedata.normalize('NFKD', cid[0]).encode('ascii','ignore')
    
    for pagei in range(1, lastpage):
        c.execute("SELECT TOP 1 * FROM result_page_%d where cid = '%s'" %(pagei, cid))
        rows = c.fetchall()
        
        if rows == [] and pagei != 1:
            for coli in range(3, len(c.description)):
                data.append('|')
            continue
                
        for row in rows:
            if pagei == 1:
                data.append(unicodedata.normalize('NFKD', row[0]).encode('ascii','ignore'))
                data.append('|')
    
            for coli in range(3, len(c.description)):
                if row[coli] == True or row[coli] == False or row[coli] == None:
                    data.append(str(row[coli]))
                else:
                    data_element = unicodedata.normalize('NFKD', row[coli]).encode('ascii','ignore')
                    data_element_list = data_element.split('\n')
                    for de in data_element_list:
                        data.append(de.strip())
                data.append('|')

    data.append("\n")

for desc_element in desc:
    sys.stdout.write(desc_element)
print ""
for data_element in data:
    sys.stdout.write(data_element)

sys.exit(0)
