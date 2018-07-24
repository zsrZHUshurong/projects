# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:37:51 2018
函数：
变量(生命周期)
def 函数名()：
    指令集和
def 函数名(a,b,c,d)
    指令集和
    def 函数名(a,b,c,d)
    return()
    指令集和
@author: Administrator
"""
############
import urllib.request as r
data=r.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')
import json
data=json.loads(data)
def weather(a,b):
    print('day'+str(a))
    print('天气情况：'+str(data['list'][b]['weather'][0]['description']))
    print('')
weather(1,2)
weather(2,10)
weather(3,18)
weather(4,26)
weather(5,34)

#2
def chart(i):
    return  str('-')*int(data['list'][i]['main']['temp'])
print('这五天温度的折线图：')
print('day1:',chart(2))
print('day2:',chart(10))
print('day3:',chart(18))
print('day4:',chart(26))
print('day5:',chart(34))

#3 
def weather(day,a):
    print(str(day)+'号18点的天气信息：')
    print('温度:'+str(data['list'][a]['main'][0]['temp']))
    print('最低温度：'+str(data['list'][a]['main'][0]['temp_min']))
    print('最高温度：'+str(data['list'][a]['main'][0]['temp_max']))
    print('气压：'+str(data['list'][a]['main'][0]['pressure']))
    print( '情况：'+str(data['list'][a]['weather'][0]['description']))
weather(1,2)
weather(2,10)
weather(3,18)
weather(4,26)


weather(5,34)

city=input('Please enter the name of tne city you want to inquire:')
import urllib.request as r
data=r.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')
import json
data=json.loads(data)
main=data['list'][0]['weather'][0]['main']
print('The weather is the case:'+main)












