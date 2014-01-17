#-------------------------------------------------------------------------------
# Name:        Fetch blog data
# Purpose:     Fetch files from a specific blog
#
# Author:      Jeffrey.zeng
#
# Created:     15/01/2014
# Copyright:   (c) Jeffrey.zeng 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import re
import os
url = "http://www.fmatlab.com/"
for i in range(1,1000):
    pageHtml = urlopen(url).read().decode('utf-8')
    print(len(pageHtml))
##soup = BeautifulSoup(pageHtml)
##linksDiv = soup.find('div',class_='entry-content clearfix')
##links = linksDiv.find_all('p')
##path = 'C:\\FinanceMatlabBook\\'
##if not os.path.isdir(path):
##    os.makedirs(path)
##
##for link in links:
##    print('source url-> '+link.a['href'])
##    linkurl = link.a['href']
##    title = link.a.get_text()
##    chapter = link.contents[0]
##    print(linkurl)
##    print(chapter)
##    print(title)
##    urlretrieve(linkurl,path+'('+chapter+')'+title+'.mht')



