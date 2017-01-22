# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import re
import string

myUrl = "http://quote.eastmoney.com/stocklist.html"
user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:37.0) Gecko/20100101 Firefox/37.0'
Accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
Accept_Language = 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'

headers = {'User-Agent':user_agent}
req = urllib2.Request(myUrl, headers = headers)
myResponse = urllib2.urlopen(req)
myPage = myResponse.read()

soup = BeautifulSoup(''.join(myPage.decode('gbk')))#<class 'bs4.BeautifulSoup'>
sum_list_table = soup.find_all("div",class_="quotebody")#<class 'bs4.element.ResultSet'>
#print sum_list_table[0].text 
stockstr = sum_list_table[0].text.split("\n")#将得到的字符串转化为列表<type 'list'>
stockitems = []
f = open("stocklist.csv","w")
for line in stockstr:
    if line.find('(') > 0:
        pos1 = line.index('(')
        stockno = (line[pos1+1:pos1+7]).encode('gbk')
        stockname = (line[:pos1]).encode('gbk')
        if stockno[0:2] in ('00','30','60'):
            stockitems.append([stockno,stockname])
stockitems.sort()
for stockitem in stockitems:
    f.write(stockitem[0]+','+stockitem[1]+'\n')
f.close()
print 'Over'
