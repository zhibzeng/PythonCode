#-------------------------------------------------------------------------------
# Name:        people.py
# Purpose:
#
# Author:      jeffrey.zzeng
#
# Created:     22/01/2014
# Copyright:   (c) jeffrey.zzeng 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class People():
    """ this is entity of zhihu people"""

    def __init__(self,name,url):
        self.name = name
        self.url = url

    def getName(self):
        return self.name

    def getUrl(self):
        return self.url




