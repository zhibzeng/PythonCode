#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
# Fetch data from geek csdn and save them to databas
# using the BeautifulSoup py Module
# Author: Jeffrey.zeng
# Created:     10/01/2014
# Copyright:   (c) Administrator 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from urllib.request import urlopen
from bs4 import BeautifulSoup
import mysql.connector
import time
url = 'http://geek.csdn.net/'
#url = url.encode('utf-8')
pageByte = urlopen(url).read()
pageStr = pageByte.decode('utf8')
soup = BeautifulSoup(pageStr)
div = soup.find_all('div',class_='content_info')
conn=mysql.connector.connect(host="localhost",user="root",passwd="7165092054",db="geekcsdn",charset="utf8")
sql = "insert into news values(%s,%s,%s,%s,%s)"
cursor = conn.cursor()
today = time.strftime("%Y-%m-%d",time.localtime())
params = []
for content in div:
    param = []
    param.append('NULL')
    name =content.h4.a.getText()
    print(name)
    param.append(name)
    path = content.h4.a['href']
    print(path)
    param.append(path)
    tag_str = ''
    tags = content.find_all('div',class_='g_tag')
    print(type(tags))
    if len(tags):
        print('tags:')
        for tag in tags:
            tag_str = tag_str+tag.getText()+','
            print(tag.getText())
    tag_str = tag_str.replace('\n','')
    if len(tag_str)>0:
        tag_str = tag_str[0:-1] #Sketch the string
    param.append(tag_str)
    param.append(today)
    params.append(param)
n = cursor.executemany(sql,params)
conn.commit()
cursor.close()
conn.close()
print(n)
