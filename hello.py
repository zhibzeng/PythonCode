# -*- coding: utf-8 -*-
import urllib
import urllib2

print('hellosss')
for i in range(1,10):
    print(i)

content = urllib2.urlopen('http://www.baidu.com')
content = content.read()
print(content)
