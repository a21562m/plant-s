 #encoding='utf8'
import urllib2

import hostaData

from bs4 import BeautifulSoup

import csv



response = urllib2.urlopen('file:///C:/xf/hosta.html')

#response = urllib2.urlopen('http://myhostas.be/db/view/Echigo+Nishiki')
html=unicode(response.read(),"ISO-8859-1")
response.close()

hosta = BeautifulSoup(html,"html.parser")
hostaName="abc"
hostaLine = hostaData.HostaData(hostaName)
for div in hosta.find_all('div'):
    input = div.find('input')
    if input is not None:
        lable=input.find_parent()
        #print lable.contents
        if "Hosta" in lable.contents[0]:
            hostaLine.Hosta=input['value'] 
     
        if "Originator:" in lable.contents[0]:
            hostaLine.Originator=input['value'] 

        if "Origin:" in lable.contents[0]:
            hostaLine.Origin=input['value'] 
            
        if "Size:" in lable.contents[0]:
            hostaLine.Size=input['value']   
            
        if "Veins:" in lable.contents[0]:
            hostaLine.Veins=input['value']             
            
        if "Leaf:" in lable.contents[0]:
            if "width:250" in input['style']:
                hostaLine.Leaf2=input['value']
            else:
                hostaLine.Leaf=input['value']             
            
        if "Leafcolor:" in lable.contents[0]:
            hostaLine.Leafcolor=input['value']             
            
        if "Var:" in lable.contents[0]:
            hostaLine.Var=input['value']             
            
        if "Leaf:" in lable.contents[0]:
            hostaLine.Leaf2=input['value']             
            
        if "Petiole:" in lable.contents[0]:
            hostaLine.Petiole=input['value']            
            
        if "Period:" in lable.contents[0]:
            hostaLine.Period=input['value']     

        if "Flower:" in lable.contents[0]:
            hostaLine.Flower=input['value'] 

split='","'  
insert = 'insert into hosta values(\"'                                        
line=insert+hostaLine.Hosta+split+hostaLine.Originator+split+hostaLine.Origin+split+hostaLine.Size+split+hostaLine.Veins+split+hostaLine.Leaf+split+hostaLine.Leafcolor+split+hostaLine.Var+split+hostaLine.Leaf2+split+hostaLine.Petiole+split+hostaLine.Flower+split+hostaLine.Period
line=line.encode('utf-8').strip()
f = open('test.csv','w')
f.write(line)
f.close()
   



