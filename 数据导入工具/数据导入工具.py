#encoding:UTF-8
import urllib.request
import bs4
from bs4 import BeautifulSoup  
import smtplib  
from email.mime.text import MIMEText  
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
hdr = {
    'Accept-Language' : 'zh-CN',
    'Accept-Charset' : 'utf-8',
    'User-Agent' : 'Mozilla/5.0 (MSIE 9.0; qdesk 2.5.1277.202; Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
}
url = 'http://weixin.sogou.com/gzh?openid=oIWsFtz_uXje1pAqkhYLJ-zh4o7g&ext=HzerOQ8mEsUPR2ztrNngpHckc3VCbu4Xc-7jMGnjOkkmA_QvWvHhfh09T-VrxAXl'
#url='http://www.python.org'
data={}
req = urllib.request.Request(url,headers=headers)
data=urllib.request.urlopen(url).read()  
z_data=data.decode('gbk','ignore')
#print(data.decode('utf-8','ignore').encode('gbk','ignore'))
soup = BeautifulSoup(data)
title = soup.find('title')
articles=soup.find('div',id='wxbox')
#print(articles)
#print(title)

 