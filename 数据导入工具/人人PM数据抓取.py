from selenium import webdriver
from bs4 import BeautifulSoup
import re,time
#driver =webdriver.PhantomJS(executable_path='D:\Python34\Scripts\phantomjs.exe')
#driver.get('http://weixin.sogou.com/weixin?query=%E9%BE%99%E6%BA%90%E7%BD%91&type=2&page=2&ie=utf8')

#driver.find_element_by_id('sogou_next').click()
#data=driver.find_element_by_class_name('results').text
#print(data)
#num=driver.find_element_by_class_name('mun').text
#print(num)

driver =webdriver.PhantomJS(executable_path='D:\Python34\Scripts\phantomjs.exe')
for i in range(1,10):
    driver.get('http://www.woshipm.com/page/%s?nocache'%i)
    result=driver.page_source
    soup = BeautifulSoup(result)
    for article in soup.findAll(class_='ft'):
        if(article.find('h3',class_='list-h3')==None):
            continue
        title=article.find('h3',class_='list-h3').find('a').string
        time=article.find(class_='time').string
        print('%s,%s'%(title,time))
print("done")


