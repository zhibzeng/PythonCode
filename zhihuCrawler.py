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
import os
from People import People
import queue

def config_init():
    """initial configuration"""
    cookie = http.cookiejar.CookieJar()
    cookie_support = urllib.request.HTTPCookieProcessor(cookie)
    proxy_handle = urllib.request.ProxyHandler({'http':'http://10.56.192.29:8080'})
    opener = urllib.request.build_opener(proxy_handle,cookie_support) # add proxy and cookie
    urllib.request.install_opener(opener)



def login(email,psw):
    """ login to zhihu.com and return the main page bytes"""
    postdata = urllib.parse.urlencode({
        'email':email,
        'password':psw
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
    main_page = urllib.request.urlopen(req)
    return main_page


def FetchPage(url,data):
    """ Fetch page, data type is dict"""
    postdata = None
    if not (data==None) :
        postdata = urllib.parse.urlencode(data)
        postdata = postdata.encode('UTF-8')
    headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0',
            'Referer':'http://www.zhihu.com'
            }
    if not (postdata==None):
        req = urllib.request.Request(
                headers = headers,
                url = url,
                data = postdata
            )
    else:
        req = urllib.request.Request(
                headers = headers,
                url = url,
            )
    page = urllib.request.urlopen(req)
    return page




if __name__ == '__main__':
    email='zengzhibin054@gmail.com'
    psw = '7165092054'
    domain = 'http://www.zhihu.com'
    config_init()  #initial configuratin
    main_page = login(email,psw) #login zhihu.com
    main_soup = BeautifulSoup(main_page.read().decode('utf-8'))

    peopleQueue = queue.Queue()
    urlQueue = queue.Queue()

    ## profile page
    profile_tag = main_soup.find('div',class_='top-nav-profile')
    profile_link = domain+profile_tag.a['href']
    profile_name = profile_tag.a.span.getText()
    me = People(profile_name,profile_link)
    peopleQueue.put(me)

    count = 0
    ## followees page
    while peopleQueue.qsize() > 0:
        item = peopleQueue.get()
        print('link -> '+item.getUrl())
        print('name -> '+item.getName())
        followees_pages = FetchPage(item.getUrl()+r'/followees',None)
        followees_soup = BeautifulSoup(followees_pages)
        followees_links = followees_soup.find_all('div',
            class_='zm-profile-card zm-profile-section-item zg-clear no-hovercard')
        for followee in followees_links:
            link = domain+followee.a['href']
            name = followee.a['title']
            person = People(name,link)
            peopleQueue.put(person)
        count = count + 1
        print(count)
        if count >100:
            break



