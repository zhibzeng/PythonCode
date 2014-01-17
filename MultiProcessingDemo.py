#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      I304905
#
# Created:     17/01/2014
# Copyright:   (c) I304905 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import threading
import datetime
import time
from urllib.request import urlopen
from urllib.request import ProxyHandler
from urllib.request import build_opener
from urllib.request import HTTPHandler
from urllib.request import install_opener
import queue
## Thread Demostration By Jeffrey.zeng
##class ThreadClass(threading.Thread):
##    def run(self):
##        now = datetime.datetime.now()
##        print('{0} says Hello World at {1}'.format(self.getName(),now))
##
##
##for i in range(2):
##    t = ThreadClass()
##    t.start()


## Grab web page from host in a ordinary way
##hosts = ["http://yahoo.com", "http://google.com", "http://amazon.com",
##        "http://ibm.com", "http://apple.com","http://baidu.com",
##        "http://taobao.com","http://sina.com"]
###set proxy server
##proxy_support = ProxyHandler({'http':'http://proxy.wdf.sap.corp:8080'})
##opener = build_opener(proxy_support, HTTPHandler)
##install_opener(opener)
##start = time.time()
###grabs urls of hosts and prints first 1024 bytes of page
##for host in hosts:
##    url = urlopen(host)
##    print(url.read(1024))
##print('elapsed for grab sepcific host url is %d'%(time.time()-start))



hosts = ["http://yahoo.com", "http://google.com", "http://amazon.com",
        "http://ibm.com", "http://apple.com"]
##proxy_support = ProxyHandler({'http':'http://proxy.wdf.sap.corp:8080'})
##opener = build_opener(proxy_support, HTTPHandler)
##install_opener(opener)

q = queue.Queue()

class ThreadUrl(threading.Thread):
    """Thread Url Grab"""
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            host = self.queue.get()
            #print(host+self.getName())
            url = urlopen(host)
            #print(url.read())
            self.queue.task_done()

start = time.time()
print(start)
def main():
    for i in range(5):
        t = ThreadUrl(q)
        t.setDaemon(True)
        t.start()


#populate queue with data
for host in hosts:
    q.put(host)
    print(host)
#wait on the queue until everything has been processed
q.join()
main()
print ("Elapsed Time: %s" %(time.time() - start))

