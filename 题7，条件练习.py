# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 16:57:38 2018
for 对于
while 当...时候
@author: Administrator
"""
import urllib.request as r
data=r.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')
import json
data=json.loads(data)
#多选一

def day(a,b):
    print('第'+str(a)+'天')
    print('温度'+str(data['list'][b]['main']['temp']))
    print('天气情况'+str(data['list'][b]['weather'][0]['description']))
    a=str(data['list'][b]['weather'][0]['main'])
    if a=='Clear':
        print('天气晴朗，适合外出。')
    elif a=='Clouds':
        print('天气多云，适合郊游。')
    elif a=='Rain':
        print('天下雨，不宜外出。')
day(1,2)
day(2,10)
day(3,18)
day(4,26)
day(5,34)
#循环
def tb():
    for a in range(0,36):
        print('第'+str(a+1)+'件商品：')
        print('标题'+str(data['mods']['itemlist']['data']['auctions'][a]['title']))
        print('价格'+str(data['mods']['itemlist']['data']['auctions'][a]['view_price']))
        print('销量'+str(data['mods']['itemlist']['data']['auctions'][a]['view_sales']))
        if(a+1)%4==0:
           print('*'*50)
        while a==40:
            continue
        if a==35:
            break
tb()
        
        
        
        
        
        
        
        
        
        




