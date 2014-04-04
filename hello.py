#-------------------------------------------------------------------------------
# Name:        SWJTU_DEAN_Crawler
# Purpose:
#
# Author:      I304905
#
# Created:     20/01/2014
# Copyright:   (c) I304905 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import urllib
import urllib2
import cookielib
import sys
from PyQt4 import QtGui

def main():
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    # build post data
    postdata = urllib.urlencode({
        '__VIEWSTATE':'/wEPDwUJOTI5NDc0OTc5D2QWAmYPZBYGAgMPZBYCAgEPZBYEAgEPFgIeC18hSXRlbUNvdW50AgcWDmYPZBYCZg8VBBEyMDE0LzMvMjUgODoyNjowOB7nvorluILooZfkuIvnqb/oh7Pkurropb/ot6/lj6MM55Sx5YyX5b6A5Y2XJ+i9pui+huaOkuihjOi+g+mVv++8jOihjOmptumAn+W6pue8k+aFomQCAQ9kFgJmDxUEETIwMTQvMy8yNSA4OjI2OjA4G+eQieeSg+eri+S6pOiHs+ahgua6queri+S6pAznlLHopb/lvoDkuJwn6L2m6L6G5o6S6KGM6L6D6ZW/77yM6KGM6am26YCf5bqm57yT5oWiZAICD2QWAmYPFQQRMjAxNC8zLzI1IDg6MjY6MDgh6Z2Z5bGF5a+66Lev5Y+j6Iez5Y+M5qGl5a2Q56uL5LqkDOeUseWMl+W+gOWNlyfovabovobmjpLooYzovoPplb/vvIzooYzpqbbpgJ/luqbnvJPmhaJkAgMPZBYCZg8VBBEyMDE0LzMvMjUgODoyNjowOB7ooaPlhqDlupnnq4vkuqToh7PmsLjkuLDnq4vkuqQM5Y2X5YyX5Y+M5ZCRJ+i9pui+huaOkuihjOi+g+mVv++8jOihjOmptumAn+W6pue8k+aFomQCBA9kFgJmDxUEETIwMTQvMy8yNSA4OjI2OjA4IeeBq+i9puWNl+ermeeri+S6pOiHs+S6uuWNl+eri+S6pAznlLHljZflvoDljJcn6L2m6L6G5o6S6KGM6L6D6ZW/77yM6KGM6am26YCf5bqm57yT5oWiZAIFD2QWAmYPFQQRMjAxNC8zLzI1IDg6MjY6MDge6JCl6Zeo5Y+j56uL5Lqk5b6A5oiQ5rip56uL5LqkDOeUseWNl+W+gOWMlyfovabovobmjpLooYzovoPplb/vvIzooYzpqbbpgJ/luqbnvJPmhaJkAgYPZBYCZg8VBBEyMDE0LzMvMjUgODoyNjowOBvlj4zmpaDnq4vkuqTlvoDmsLjkuLDnq4vkuqQM55Sx5Y2X5b6A5YyXJ+i9pui+huaOkuihjOi+g+mVv++8jOihjOmptumAn+W6pue8k+aFomQCAw8PFgQeEEN1cnJlbnRQYWdlSW5kZXgCAh4LUmVjb3JkY291bnQCFmRkAgUPDxYCHgRUZXh0BQQxNDE5ZGQCBw8PFgIfAwUIMTI3Nzg2ODhkZGQIRPzkIDg5iluWfoOBZAOJrefYZSrqmwCzLvdpd1u9ZQ==',
        '__EVENTTARGET':'ctl00$ContentPlaceHolder1$AspNetPager1',
        '__EVENTARGUMENT':'1',
        '__EVENTVALIDATION':'/wEdAALzHc+0D0mQQjct7R82rwk35UDzBtAvn5Vse6EOGRvssrOfTCVtxzxeh5JbmrdRFfBKV+6H+n9pX+CDvW1WiD9z',
        'ctl00$ContentPlaceHolder1$hidXxlx':''
    })
    headers = {
            'Host':'www.cdjg.gov.cn',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:29.0) Gecko/20100101 Firefox/29.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':'en-US,en;q=0.5',
            'Accept-Encoding':'gzip, deflate',
            'Referer':'http://www.cdjg.gov.cn/WebService/TrffYdxx.aspx',
            'Connection':'keep-alive'
                }
    postdata = postdata.encode('UTF-8') # convert postdata from str to bytes
    #send request
    req = urllib2.Request(
        headers = headers,
        url = 'http://www.cdjg.gov.cn/WebService/TrffYdxx.aspx',
        data = postdata
    )
    result = opener.open(req)
    print(result.read().decode('utf-8'))
    for item in cookie:
        print('name %s'%(item.name))
        print('value %s'%(item.value))

def FetchEnglishListening():
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    headers = {
            'Host':'http://www.kekenet.com/',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:29.0) Gecko/20100101 Firefox/29.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':'en-US,en;q=0.5',
            'Accept-Encoding':'gzip, deflate',
            'Referer':'http://www.kekenet.com/',
            'Connection':'keep-alive'
                }
     #send request
    req = urllib2.Request(
        headers = headers,
        url = 'http://www.baidu.com/'
    )
    result = opener.open(req)
    print(result.read().decode('utf-8'))
    for item in cookie:
        print('name %s'%(item.name))
        print('value %s'%(item.value))

def youjia():
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    headers = {
           'Host':'youjia.15tianqi.cn',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:29.0) Gecko/20100101 Firefox/29.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':'en-US,en;q=0.5',
            'Accept-Encoding':'gzip, deflate',
            'Referer':'http://youjia.15tianqi.cn/chengdu/'
    }
     #send request
    req = urllib2.Request(
        headers = headers,
        url = 'http://youjia.15tianqi.cn/chengdu/'
    )
    result = opener.open(req)
    print(result.read())


def qt():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    sys.exit(app.exec_())


import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

def QtWebKit():
    class Render(QWebPage):
        def __init__(self, url):
            self.app = QApplication(sys.argv)
            QWebPage.__init__(self)
            self.loadFinished.connect(self._loadFinished)
            self.mainFrame().load(QUrl(url))
            self.app.exec_()

        def _loadFinished(self, result):
            self.frame = self.mainFrame()
            self.app.quit()
    url = 'http://webscraping.com/'
    r = Render(url)
    html = r.frame.toHtml()
    print html


from selenium import webdriver
import sys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
def testSelenium():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    driver = webdriver.PhantomJS()
    driver.get('http://www.bitauto.com/youjia/')
    data1 = driver.find_element_by_id('login_nav').text
    #data2 = data = driver.find_elements(By.CLASS_NAME, 'oilTableOut')
    data2 = data = driver.find_elements_by_class_name('oilTableOut')
    html_source = driver.page_source
    #print html_source
    soup = BeautifulSoup(html_source)
    sichuan = soup.select("body > div.bt_page > div.bt_page > div > div.oilTableOut > table > tbody > tr:nth-of-type(11) > th:nth-of-type(2) > a")
    #90号汽油
    type1 = soup.select("body > div.bt_page > div.bt_page > div > div.oilTableOut > table > tbody > tr:nth-of-type(11) > td:nth-of-type(5)")
    #93号汽油
    type2 = soup.select("body > div.bt_page > div.bt_page > div > div.oilTableOut > table > tbody > tr:nth-of-type(11) > td:nth-of-type(6)")
    #97号汽油
    type3 = soup.select("body > div.bt_page > div.bt_page > div > div.oilTableOut > table > tbody > tr:nth-of-type(11) > td:nth-of-type(7)")
    #0号柴油(元/升)
    type4 = soup.select("body > div.bt_page > div.bt_page > div > div.oilTableOut > table > tbody > tr:nth-of-type(11) > td:nth-of-type(8)")
    print sichuan[0].get_text()
    print type1[0].get_text()
    print type2[0].get_text()
    print type3[0].get_text()
    print type4[0].get_text()
    print driver.current_url
    driver.quit

if __name__ == '__main__':
    #main()
    #FetchEnglishListening()
    #youjia()
    #FetchEnglishListening()
    #qt()
    #QtWebKit()
    testSelenium()
