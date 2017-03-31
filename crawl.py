#Date: 2017.03.30
#Author: RyQ
#Name: Billboard crawler
#Ver:0.9

# -*- coding: utf-8 -*-

import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

header={
    'DNT': '1',\
    'Referer': 'http://www.billboard.com/',\
    'Upgrade-Insecure-Requests':'1',\
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',\
    'Cache-Control': 'max-age=0',\
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8'
}

def get_html(url):
    print "Get html"
    html=requests.get(url,headers=header).text
    return html

url='http://www.billboard.com/charts/hot-100'
f=open('test.html','w')
print >> f,get_html(url)
f.close()