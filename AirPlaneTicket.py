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
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as tree
import urllib.request

def main():
    context = urllib.request.urlopen('http://ws.qunar.com/holidayService.jcp?lane=上海-长沙')
    tree = etree.parse(context)
    root = tree.getroot()
    for node in root[0]:
        if node.attrib["date"] == "2011-09-30":
            for child in node:
                for child_detail in child.attrib.keys():
                    if child.attrib["type"] == "go" and int(child.attrib["price"])<600:
                        print(child_detail,child.attrib[child_detail])
                        urllib.urlopen('http://api.sms.xxx.com/sms.jcp?c="有机票了"&p=138********'

