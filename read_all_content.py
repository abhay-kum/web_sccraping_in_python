#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 00:53:34 2018

@author: abhay
"""

import bs4 as bs
import urllib.request
import pandas as pd

##------------------------data to fetch from the website##################

details=['Name of the Company','Contact Person','Designation','Street Address','City','State'
         ,'Pincode','Email','Phone','Mobile','Fax','Website']

Na=[]
Contact=[]
De=[]
Street=[]
City=[]
State=[]
Pincode=[]
Email=[]
Phone=[]
Mobile=[]
Fax=[]
Website=[]


link=pd.read_csv('website_list.csv')

print(link['Address'].head())

#link=['http://www.iato.in/members/view/1925 ',
#      'http://www.iato.in/members/view/11402', 
#      'http://www.iato.in/members/view/1844',
#      'http://www.iato.in/members/view/2053',
#      'http://www.iato.in/members/view/314']

for url in link['Address']:
    source=urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source,'html5lib')
    te=[]
    for p_tags in  soup.find_all('p'):
        te.append(p_tags.text)
        print(p_tags.text)
    
    cont=[]
    for t in te:
        cont.append(t.split(':'))
    
    for i in range(0,len(cont)):
       if details[0] in cont[i]:
           Na.append(cont[i][1])
       if details[1] in cont[i]:
           Contact.append(cont[i][1])
       if details[2] in cont[i]:
           De.append(cont[i][1])
       if details[3] in cont[i]:
           Street.append(cont[i][1])
       if details[4] in cont[i]:
           City.append(cont[i][1])
       if details[5] in cont[i]:
           State.append(cont[i][1])
       if details[6] in cont[i]:
           Pincode.append(cont[i][1])
       if details[7] in cont[i]:
           Email.append(cont[i][1])
       if details[8] in cont[i]:
           Phone.append(cont[i][1])
       if details[9] in cont[i]:
           Mobile.append(cont[i][1])
       if details[10] in cont[i]:
           Fax.append(cont[i][1])
       if details[11] in cont[i]:
           Website.append(cont[i][1])


del(Mobile[1659])
data={details[0]:Na,details[1]:Contact,details[2]:De,details[3]:Street,details[4]:City,
      details[5]:State,details[6]:Pincode,details[7]:Email,details[8]:Phone,details[9]:Mobile,
       details[10]:Fax,details[11]:Website }

df=pd.DataFrame(data)
df.to_csv('content_deatils.csv')
