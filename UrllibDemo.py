#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      I304905
#
# Created:     20/01/2014
# Copyright:   (c) I304905 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import urllib.request
import http.cookiejar
import urllib.parse
def proxyDemo():
    """Demostration how to set a proxy and header in urllib"""
    proxy = urllib.request.ProxyHandler({'http':'http://proxy.wdf.sap.corp:8080'})
    opener = urllib.request.build_opener(proxy) # add proxy
    urllib.request.install_opener(opener)
    req = urllib.request.Request('http://www.baidu.com')
    req.add_header('User-Agent', 'fake-client') #add a header
    response = urllib.request.urlopen(req,timeout=10).read() # set a timeout
    print(response.decode('utf-8'))

def redirectDemo():
    url = 'http://www.google.com'
    response = urllib.request.urlopen(url)
    print('original url %s'%(url))
    print('new url %s'%(response.geturl()))

def cookieDemo():
    cookie = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    response = opener.open('http://www.baidu.com')
    for item in cookie:
        print('Name:%s--Value:%s'%(item.name,item.value))

def httpResponseCodeDemo():
    try:
        response = urllib.request.urlopen('http://www.baibai.com')
    except (urllib.request.HTTPError, e):
        print(e.code)

def debugDemo():
    httpHandler = urllib.request.HTTPHandler(debuglevel=1)
    httpsHandler = urllib.request.HTTPSHandler(debuglevel=1)
    opener = urllib.request.build_opener(httpHandler, httpsHandler)
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen('http://www.google.com')

def submitForm():
    postdata = urllib.parse.urlencode({
        'username':'汪小光',
        'password':'why888',
        'continueURI':'http://www.verycd.com/',
        'fk':'',
        'login_submit':'登录'
    })
    postdata = postdata.encode('UTF-8')
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }

    req = urllib.request.Request(
        url = 'http://www.verycd.com/signin',
        data = postdata,
        headers = headers
    )
    response = urllib.request.urlopen(req)
    print(response.read().decode('utf-8'))


if __name__ == '__main__':
    proxyDemo()
    #redirectDemo()
    #cookieDemo()
    #httpResponseCodeDemo()
    #debugDemo()
    submitForm()

