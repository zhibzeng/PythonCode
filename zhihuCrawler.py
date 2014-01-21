#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      I304905
#
# Created:     21/01/2014
# Copyright:   (c) I304905 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib.request
import http.cookiejar
import urllib.parse
from bs4 import BeautifulSoup
cookie = http.cookiejar.CookieJar()
operner = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
urllib.request.HTTPHandler
postdata = urllib.parse.urlencode({
    'email':'zengzhibin054@gmail.com',
    'password':'7165092054'
})
postdata = postdata.encode('UTF-8')
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0',
        'Referer':'http://www.zhihu.com'
        }
req = urllib.request.Request(
        headers = headers,
        url = 'http://www.zhihu.com/login',
        data = postdata
    )
main_page = operner.open(req)
main_soup = BeautifulSoup(main_page.read().decode('utf-8'))
print(main_soup.prettify())

topic_page = operner.open('http://www.zhihu.com/topic')
topic_soup = BeautifulSoup(topic_page)
links = topic_soup.find_all('a',class_='topic-item-title-link')
for link in links:
    print(link.getText())
