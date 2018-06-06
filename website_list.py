#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 19:54:43 2018

@author: abhay
"""
import bs4 as bs
import urllib.request
import pandas as pd

url="http://www.iato.in/members/lists"

source = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(source,'html5lib')

#print(soup.title)
thead=[]
table=soup.find('table')
for th in table.find_all('th'):
    thead.append(th.string)


hyper_link=[]
hyper_name=[]

for link in table.find_all('a'):
    a=link.get('href')
    n=link.string
    hyper_name.append(n)
    hyper_link.append(a)
    #print(link.get('href'))

d={thead[1]:hyper_name,thead[2]:hyper_link}
df=pd.DataFrame(data=d)
df.to_csv('website_list.csv')
