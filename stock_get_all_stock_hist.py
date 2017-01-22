# -*- coding: utf-8 -*-
import string
import urllib2
import time

user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)'
Accept = 'text/html, application/xhtml+xml, */*'
Accept_Language = 'zh-CN'
headers = {'User-Agent':user_agent}

def get_stock_hist(stockno):
    print stockno
    myUrl = "http://xueqiu.com/S/"+stockno+"/historical.csv"
    filename = stockno+".csv"
    req = urllib2.Request(myUrl, headers = headers)
    myResponse = urllib2.urlopen(req)
    myPage = myResponse.read()
    f = open(filename,'w')
    f.write(myPage)
    f.close()
    time.sleep(5)
    
stocklist = open("stocklist.csv")
lines = stocklist.readlines()
for line in lines[]:
    arr = line.replace("'",'').replace('\n','').split(',')
    stockno = arr[0]
    stocknmae = arr[1]
    if stockno[0:2] in ('00','30'):
        stockno = 'SZ'+stockno
    else:
        stockno = 'SH'+stockno
    print stockno
##    get_stock_hist(stockno)
