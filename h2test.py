# -*- coding:utf-8 -*-
import re
import urllib2
from bs4 import BeautifulSoup
inputNum=1
inputAd='北京'
inputNum=str(inputNum)
addr='http://www.11315.com/search?name='+inputAd+'&regionDm=&page='+inputNum
headers={'User-Agent':'Mozilla/5.0(Windows;U;Windows NT 6.1;en-US;rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
req=urllib2.Request(url=addr,headers=headers)
content=urllib2.urlopen(req).read()
t=content.decode('utf-8')
bsss=BeautifulSoup(t,"lxml")
conames=bsss.find_all('h2',{'class':'con-name'})
for coname in conames:
	coname=str(coname).decode('utf-8')
	conameaddr=BeautifulSoup(coname,"lxml").a['href']
	coreq=urllib2.Request(url=conameaddr,headers=headers)
	cocontent=urllib2.urlopen(coreq).read()
	print cocontent
	break
