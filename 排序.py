# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 15:57:32 2018

@author: Administrator
"""
import urllib.request as r
data=r.urlopen('https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&type=p&tmhkh5=&spm=a21wu.241046-us.a2227oh.d100&from=sea_1_searchbutton&catId=100&ajax=true').read().decode('utf-8','ignore')
import json
data=json.loads(data)

ls1=[]
def price():
        for i in range(0,36):
        b=float(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
        ls1.append(b)
        return ls1
price()
c=sorted(ls1)
print('商品价格从高到低排序为：')
d=list(reversed(c))
print(c)

ls2=[]
def sales():
        for i in range(0,36):
      sales=(data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
        e=int(sales[0:-3])
        ls2.append(e)
        return ls2
sales()
f=sorted(ls2)
print('商品销量从高到低排序为：')
g=list(reversed(f))
print(g)


