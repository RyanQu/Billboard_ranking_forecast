#Date: 2017.03.30
#Author: RyQ
#Name: Billboard crawler
#Ver:0.9

# -*- coding: utf-8 -*-
import time
import random
import datetime
import requests
import sys
from bs4 import BeautifulSoup

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
    time.sleep(3*random.random())
    return html

# cha=datetime.timedelta(days=2)
# boardday=[]
# for n in xrange(0,400):
#     now=datetime.datetime.now()-cha
#     delta=datetime.timedelta(days=7*n)
#     dates=now-delta
#     past_n_weeks=dates.strftime('%Y-%m-%d')
#     boardday.append(past_n_weeks)

# print boardday

# f=open('album.csv','w')
# print >> f, '"rank","album_name","last_week","peak_position","wks_on_rank","artist_name","date"'
# f.close()

# chart_id=0
# for day in boardday:
#     chart_id=chart_id+1
#     print chart_id
#     print day
url = 'http://www.billboard.com/charts/billboard-200/2017-04-29'
html = get_html(url)
soup = BeautifulSoup(html,"html.parser")
#cur = soup(class_="chart-row")

album_cur = soup(class_="chart-row__song")
album=[]
for sp in album_cur:
    album.append(sp.text.strip().replace(',',' '))

rank_cur = soup(class_="chart-row__current-week")
rank=[]
for sp in rank_cur:
    rank.append(int(sp.text.strip()))

stats_cur = soup(class_="chart-row__stats")
lastrank=[]
peak=[]
weeks=[]
for sp in stats_cur:
    stats = sp.find_all(class_="chart-row__value")
    count = 0
    for i in stats:
        if (count == 0):
            lastrank.append(i.text)
        if (count == 1):
            peak.append(i.text)
        if (count == 2):
            weeks.append(i.text)
        count = count + 1

#print lastrank, peak, weeks

artist_cur = soup(class_="chart-row__artist")
artist=[]
for sp in artist_cur:
    artist.append(sp.text.strip().replace(',',' '))

date ='4/29/2017'
date_429=[]
for i in range(200):
    date_429.append(date)
    
# print date_415
# day_list=[]
# for i in range(200):
#     day_list.append(day)

data = zip(rank, album, lastrank, peak, weeks, artist,date_429)

f=open('429album.csv','w')
print >> f, '"rank","album_name","last_week","peak_position","wks_on_rank","artist_name","date"'
for line in data:
    line_count=0
    for ch in line:
        line_count+=1
        if line_count==7:
            print >> f,ch
        else:
            print >> f,ch,',',

f.close()

# f=open('test.html','w')
# print >> f,get_html(url)
# f.close()
