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


import queue
import threading
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup

hosts = ["http://www.baidu.com", "http://www.sina.com", "http://www.163.com",
        "http://www.qq.com", "http://www.ifeng.com"]

host_queue = queue.Queue()
out_queue = queue.Queue()

class ThreadUrl(threading.Thread):
    """Threaded Url Grab"""
    def __init__(self, queue, out_queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.out_queue = out_queue

    def run(self):
        while True:
            #grabs host from queue
            host = self.queue.get()

            #grabs urls of hosts and then grabs chunk of webpage
            url = urlopen(host)
            chunk = url.read()

            #place chunk into out queue
            self.out_queue.put(chunk)

            #signals to queue job is done
            self.queue.task_done()

class DatamineThread(threading.Thread):
    """Threaded Url Grab"""
    def __init__(self, out_queue):
        threading.Thread.__init__(self)
        self.out_queue = out_queue

    def run(self):
        while True:
            #grabs host from queue
            chunk = self.out_queue.get()

            #parse the chunk
            soup = BeautifulSoup(chunk)
            print(soup.findAll(['title']))

            #signals to queue job is done
            self.out_queue.task_done()

start = time.time()
def main():

    #spawn a pool of threads, and pass them queue instance
    for i in range(3):
        t = ThreadUrl(host_queue, out_queue)
        t.setDaemon(True)
        t.start()

    #populate queue with data
    for host in hosts:
        host_queue.put(host)

    for i in range(3):
        dt = DatamineThread(out_queue)
        dt.setDaemon(True)
        dt.start()


    #wait on the queue until everything has been processed
    host_queue.join()
    out_queue.join()

main()
print ("Elapsed Time: %s" % (time.time() - start))