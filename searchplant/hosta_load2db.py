 #encoding='utf-8'
import sys

import urllib2

import hostaData

import unicodedata

from bs4 import BeautifulSoup

import psycopg2

def vs(s):
    #s.replace("'","'''")
    return s
    
    
conn = psycopg2.connect(database="myplant", user="puser", password="Polycom123", host="140.143.19.180", port="5432")
 
print "Opened database successfully"

cur = conn.cursor()
 
cur.execute("select name,weburl,fname,id from hosta.hostaurl where flag=0 order by fname ")
rows = cur.fetchall()
f = open('test.sql','w')
for row in rows:
    id=row[3]
    hostaLine = hostaData.HostaData(row[0])
    #print "name = ", row[0], "\n"
    filename = '..\data\hosta\\' + row[2] + '.html'
    weburl ='file:///C:/Users/xfeng/fengxin/Study/bigData/plant-s/data/hosta/' + row[2] + '.html'
    #print filename
    try:
        
        #with open(filename, 'r') as f:
        #    html=f.read()
        html = urllib2.urlopen(weburl).read()
        #html=unicode(html,'GBK').encode('UTF-8')
        
        
        html = html.encode('utf-8').strip()
        
        #html=html.replace("\xc2\xa0", " ")

        #Sprint html
        
            
        #f.close()
        hosta = BeautifulSoup(html, "html.parser")
        #Sprint hosta
        
        for div in hosta.find_all('div'):
            input = div.find('input')
            if input is not None:
                lable = input.find_parent()
                # print lable.contents
                if "Hosta" in lable.contents[0]:
                    hostaLine.Hosta = input['value'].replace("'","''") 
             
                if "Originator:" in lable.contents[0]:
                    hostaLine.Originator = input['value'].replace("'","''") 
        
                if "Origin:" in lable.contents[0]:
                    hostaLine.Origin = input['value'].replace("'","''")
                    
                if "Size:" in lable.contents[0]:
                    hostaLine.Size = input['value'].replace("'","''")   
                    
                if "Veins:" in lable.contents[0]:
                    hostaLine.Veins = input['value'].replace("'","''")             
                    
                if "Leaf:" in lable.contents[0]:
                    if "width:250" in input['style']:
                        hostaLine.Leaf2 = input['value'].replace("'","''")
                    else:
                        hostaLine.Leaf = input['value'].replace("'","''")             
                    
                if "Leafcolor:" in lable.contents[0]:
                    hostaLine.Leafcolor = input['value'].replace("'","''")             
                    
                if "Var:" in lable.contents[0]:
                    hostaLine.Var = input['value'].replace("'","''")             
                    
                if "Leaf:" in lable.contents[0]:
                    hostaLine.Leaf2 = input['value'].replace("'","''")             
                    
                if "Petiole:" in lable.contents[0]:
                    hostaLine.Petiole = input['value'].replace("'","''")            
                    
                if "Period:" in lable.contents[0]:
                    hostaLine.Period = input['value'].replace("'","''")     
        
                if "Flower:" in lable.contents[0]:
                    hostaLine.Flower = input['value'].replace("'","''") 
                    
        sql = "INSERT INTO hosta.hostadata(name, originator, origin, size, veins, leaf, leafcolor, var, leaf2, petiole, flower, period, progeny)    VALUES ('"
        split="','"
        sqlValue=vs(hostaLine.Hosta)+split+vs(hostaLine.Originator)+split+vs(hostaLine.Origin)+split+vs(hostaLine.Size)+split+vs(hostaLine.Veins)+split+vs(hostaLine.Leaf)+split+vs(hostaLine.Leafcolor)+split+vs(hostaLine.Var)+split+vs(hostaLine.Leaf2)+split+vs(hostaLine.Petiole)+split+vs(hostaLine.Flower)+split+vs(hostaLine.Period)+split+vs(hostaLine.Progeny)
        sqlStatement=sql+sqlValue+"');"+"\n"
        sqlStatement=sqlStatement.encode('UTF-8')
        f.write(sqlStatement)
        #print hostaLine.Origin.replace("'","'''")
        #cur.execute(sqlStatement)
        
    except Exception,e:
        print e
        sql=sql = "update hosta.hostaurl set flag=3 where id ='"+id+"'"
        cur.execute(sql)
        cur.execute("commit")
f.close()           
cur.execute("commit")