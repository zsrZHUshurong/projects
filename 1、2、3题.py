# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
temper=[30,31,32,33,34,35,36]
print('周三'+str(temper[3])+'°')

a=['周一晴','周二阴','周三多云','周四晴','周五阴']
b=['23','24','25','27','29']
print('天气：'+a[0]+' '+'温度：'+b[0])
print('天气：'+a[1]+' '+'温度：'+b[1])
print('天气：'+a[2]+' '+'温度：'+b[2])
print('天气：'+a[3]+' '+'温度：'+b[3])
print('天气：'+a[4]+' '+'温度：'+b[4])


print(a)
import urllib.request as r
data=r.urlopen('http://api.openweathermap.org/data/2.5/weather?q=chongqing&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996').read().decode('utf-8','ignore')


import json
data=json.loads(data)
data['main']['temp']
data['wind']['speed']
data['main']['pressure']
temper=[30,31,32,33,34,35,36]
print('周三'+str(temper[3])+'°')

a=['周一晴','周二阴','周三多云','周四晴','周五阴']

import urllib.request as r
data=r.urlopen('http://api.openweathermap.org/data/2.5/weather?q=chongqing&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996').read().decode('utf-8','ignore')


import json
data=json.loads(data)

print(data['main']['temp'])
print(data['weather'][0]['description'])
print(data['main']['pressure'])
print(data['wind']['speed'])



















