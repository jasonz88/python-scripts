import sys,time
from math import tan,radians,pi
from xml.dom.minidom import parseString

def getParameter(tagName,document):
    dom = parseString(document)
    xmlTag = dom.getElementsByTagName(tagName)[0].toxml()
    xmlData=xmlTag.replace('<'+tagName+'>','').replace('</'+tagName+'>','')
    return float(xmlData)

def intersection(x1,y1,d1,x2,y2,d2):
    if d1==d2 or d1+d2==2.0*pi:
        return (x1+x2)/2.0,(y1+y2)/2.0
    elif d1==pi*0.5 or d1==pi*1.5:
        return x1,(x1-x2)*tan(d2)+y2
    elif d2==pi*0.5 or d2==pi*1.5:
        return x2,(x2-x1)*tan(d1)+y1
    else:
        return (x1*tan(d1)-x2*tan(d2)+y2-y1)/(tan(d1)-tan(d2)),\
            ((x1-x2)*tan(d1)*tan(d2)+tan(d1)*y2-tan(d2)*y1)/(tan(d1)-tan(d2))

def main():
    st=time.clock()
    fh=open(sys.argv[1],'r')
    array=[]
    res=[]
    info=fh.read()
    fh.close()
    dom = parseString(info)
    for i in range(3):
                array.append([])
    p=dom.getElementsByTagName('photo').length            
    for i in range(p):
                pic = dom.getElementsByTagName('photo')[i].toxml()
                array[0].append(getParameter('longitude',pic))
                array[1].append(getParameter('latitude',pic))
                array[2].append(getParameter('direction',pic))
    l=len(array[0])
    res.append([])
    res.append([])
    for i in range(l):
        for j in range(i,l):
            (ix,iy)=intersection(array[0][i],array[1][i],array[2][i],\
                                 array[0][j],array[1][j],array[2][j])
            res[0].append(ix)
            res[1].append(iy)
        et=time.clock()
        print sum(res[0])/float(l), sum(res[1])/float(l)
        #print et-st
        return sum(res[0])/float(l), sum(res[1])/float(l)

if __name__ == "__main__":
        main()
