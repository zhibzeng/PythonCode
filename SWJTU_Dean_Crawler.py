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
import urllib.request
import http.cookiejar
import urllib.parse
from bs4 import BeautifulSoup

def main():
    cookie = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    # build post data
    postdata = urllib.parse.urlencode({
        'password':'********',
        'url':'../usersys/simple.jsp',
        'user_id':'20103375',
        'user_style':'old',
        'user_type':'student'
    })
    postdata = postdata.encode('UTF-8') # convert postdata from str to bytes
    #send request
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0',
        'Referer':'http://202.115.67.2/service/login.jsp?user_type=student'
        }
    req = urllib.request.Request(
        headers = headers,
        url = 'http://202.115.67.2/servlet/UserLoginSQLAction',
        data = postdata
    )
    result = opener.open(req)
    print(result.read().decode('gb2312'))
    for item in cookie:
        print('name %s'%(item.name))
        print('value %s'%(item.value))

    print('main content...')
    content = opener.open('http://202.115.67.2/usersys/simple.jsp')
    #print(content.read().decode('utf-8'))


    print('Before Score...')
    beforScore = opener.open('http://202.115.67.2/servlet/CheckStudentSubmitAppraiseAction')
    #print(beforScore.read().decode('utf-8'))

    print('scorepage...')
    scorepage = opener.open('http://202.115.67.2/student/score/ScoreNew.jsp?SelectType=ALL')
    #print(scorepage.read().decode('utf-8'))
    soup = BeautifulSoup(scorepage.read())
    scoreTable = soup.find(id='table7')
    items = scoreTable.find_all('tr')
    for item in items:
        print(item.contents)

if __name__ == '__main__':
    main()
