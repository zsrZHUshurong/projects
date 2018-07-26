# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 20:22:05 2018

@author: Administrator
"""
f=open('山东招生人数.txt',encoding='gbk').readlines()
schoolls=[]
data=[]
for line in f:
    schoolls.append(line.split('(')[1].split(',')[0])
    data.append(line.split(',')[1].split(')')[0])
    print(schoolls)
    print(data)