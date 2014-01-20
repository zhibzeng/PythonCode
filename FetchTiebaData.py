#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      I304905
#
# Created:     20/01/2014
# Copyright:   (c) I304905 2014
# Licence:     <your licence>
#---------------------------------------
#   程序：百度贴吧爬虫
#   语言：Python 3.3
#   操作：输入带分页的地址，去掉最后面的数字，设置一下起始页数和终点页数。
#   功能：下载对应页码内的所有页面并存储为html文件。
#---------------------------------------
import string, urllib.request

#定义百度函数
def baidu_tieba(url,begin_page,end_page):
    for i in range(begin_page, end_page+1):
        sName = str(i)+ '.html'#自动填充成六位的文件名
        print('正在下载第' + str(i) + '个网页，并将其存储为' + sName + '......')
        f = open(sName,'w+')
        m = urllib.request.urlopen(url + str(i)).read().decode('gbk')
        f.write(m)
        f.close()
#bdurl = 'http://tieba.baidu.com/p/2296017831?pn='
#iPostBegin = 1
#iPostEnd = 10
bdurl = str(input(u'请输入贴吧的地址，去掉pn=后面的数字：\n'))
begin_page = int(input(u'请输入开始的页数：\n'))
end_page = int(input(u'请输入终点的页数：\n'))
#调用
baidu_tieba(bdurl,begin_page,end_page)
