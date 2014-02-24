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
import io
import gzip
import threading
import time

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
    try:
        page = urllib.request.urlopen(req)
    except:
        print('fetch page error')
    ## using gzip to fetch page
    if page.code == 200:
        predata = page.read().decode('utf-8')
        pdata = io.StringIO(predata)
        gzipper = gzip.GzipFile(fileobj = pdata)
        try:
            pagedata = gzipper.read()
            print('gzip')
        except:
            # if the server don't support gzip download directly
            pagedata = predata
    else:
        return None
    page.close()
    return pagedata


class ThreadUrl(threading.Thread):
    """Threaded Url Grab"""
    def __init__(self, queue,out_queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.out_queue = out_queue

    def run(self):
        while True:
            global count
            global domain
            global peopleNum # the number of people you want to fetch
            #grabs url from queue
            item = self.queue.get()
            self.out_queue.put(item)
            if count<peopleNum:
                #grabs urls of people and then grabs chunk of webpage
                followees_pages = FetchPage(item.getUrl()+r'/followees',None)
                followees_soup = BeautifulSoup(followees_pages)
                followees_links = followees_soup.find_all('div',
                class_='zm-profile-card zm-profile-section-item zg-clear no-hovercard')
                for followee in followees_links:
                    link = domain+followee.a['href']
                    name = followee.a['title']
                    person = People(name,link)
                    if count<peopleNum:
                        self.queue.put(person)
                        count = count+1
            #signals to queue job is done
            self.queue.task_done()


class DatamineThread(threading.Thread):
    """Threaded Url Grab"""
    def __init__(self, out_queue):
        threading.Thread.__init__(self)
        self.out_queue = out_queue

    def run(self):
        while True:
            #grabs item from queue
            item = self.out_queue.get()
            print('name->'+item.getName())
            print('link->'+item.getUrl())
            #signals to queue job is done
            self.out_queue.task_done()


def main(thread):
    ThreadNum = thread
    email='zengzhibin054@gmail.com'
    psw = '********'
    config_init()  #initial configuratin
    main_page = login(email,psw) #login zhihu.com
    main_soup = BeautifulSoup(main_page)
    peopleQueue = queue.Queue()
    outQueue = queue.Queue()
    ## profile page
    profile_tag = main_soup.find('div',class_='top-nav-profile')
    profile_link = domain+profile_tag.a['href']
    profile_name = profile_tag.a.span.getText()
    me = People(profile_name,profile_link)
    peopleQueue.put(me)
    for i in range(ThreadNum):
        t = ThreadUrl(peopleQueue,outQueue)
        t.setDaemon(True)
        t.start()
    for i in range(ThreadNum):
        t = DatamineThread(outQueue)
        t.setDaemon(True)
        t.start()
    outQueue.join()
    peopleQueue.join()

if __name__ == '__main__':
    i=2
    start = time.time()
    count = 1
    domain = 'http://www.zhihu.com'
    peopleNum = 20 # the number of people you want to fetch
    main(i)
    elapsed = time.time() - start
    print(str(count))
    print ("Elapsed Time: %s" % (elapsed))
    print('threadNum:'+str(i))
    f = open('zhihu.txt','a')
    s = 'count:'+str(count)+','+'Thread:'+str(i)+','+'elapsed:'+str(elapsed)
    f.write(s+'\n')
    f.close()



