# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 10:13:19 2018

@author: Administrator
"""
import json
import urllib.request as r
import time
word = r.quote('裙子')
url = 'https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20180719&stats_click=search_radio_all%3A1&js=1&imgfile=&q=%E8%A3%99%E5%AD%90&suggest=history_3&_input_charset=utf-8&wq=&suggest_query=&source=suggest&loc=%E5%AE%81%E6%B3%A2&ajax=true' 
itemList = []
def reqTimeOut(url,timeOut):
    for i in range(50,100):
        urlPage = url + '&s=' + str(i*44)
        try:
            req = r.urlopen(urlPage)
            if req.getcode()==200:
                data = req.read().decode('utf-8','ignore')
        except Exception as err:
            print('网络请求错误,正在重试中。。。')
            i = i-1
            break
      # data = json.loads(data)
        try:
            fileURL = open('reqData.txt','a+',encoding='utf-8')
#            fileList = open('reqList.txt','w',encoding='utf-8')
            fileURL.write(data+'\n')
            fileURL.close()
        except Exception as err:
            print('文件写入错误！重试中。。。')
            break
    # itemList.append(data['mods']['itemlist']['data']['auctions'])
        print('爬取第'+str(i+1)+'页成功')
        time.sleep(timeOut)
reqTimeOut(url,0)
