#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     15/01/2014
# Copyright:   (c) Administrator 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
url = "http://www.fmatlab.com/"
pageHtml = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(pageHtml)
linksDiv = soup.find('div',class_='entry-content clearfix')
links = linksDiv.find_all('p')

for link in links:
    print('source url-> '+link.a['href'])
