# -*- coding: utf-8 -*-
import string
import os

stocklist = open("stocklist.csv")
stocksum = open("stocksum.csv",'w')
lines = stocklist.readlines()
for line in lines:
    arr = line.replace("'",'').replace('\n','').split(',')
    stockno = arr[0]
    stocknmae = arr[1]
    if stockno[0:2] in ('00','30'):
        stockno = 'SZ'+stockno
    else:
        stockno = 'SH'+stockno        
        
    filename = "./hist/"+stockno+".csv"
    if not os.path.isfile(filename):
        continue
    stockhist = open(filename)
    lines = stockhist.readlines()
    stocksum.write(stockno+','+stocknmae+','+str(len(lines))+'\n')
stocksum.close()
