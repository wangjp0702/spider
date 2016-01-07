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
#driver.get('http://weixin.sogou.com/gzh?openid=oIWsFtz_uXje1pAqkhYLJ-zh4o7g&ext=HzerOQ8mEsUPR2ztrNngpHckc3VCbu4Xc-7jMGnjOkkmA_QvWvHhfsJSqNtij-hS')
#cookie=driver.get_cookies()

driver.add_cookie({'name':'ABTEST', 'value':'3|1449821001|v17','domain':'www.sogou.com','path':'/'})
driver.add_cookie({'name':'ppmdig', 'value':'1449823942000000bf344f028f0e9e6fccbd13045fd700f4','domain':'www.sogou.com','path':'/'})
driver.add_cookie({'name':'ppmdig', 'value':'1449823942000000ae96771a15cab107e6490b5bf1bd42d3','domain':'weixin.sogou.com','path':'/'})
driver.add_cookie({'name':'FINSG', 'value':'old','domain':'.www.sogou.com','path':'/'})
driver.add_cookie({'name':'taspeed', 'value':'taspeedexist','domain':'.www.sogou.com','path':'/'})
driver.add_cookie({'name':'endorse_friendship_update', 'value':'9367C14E481087FBD30D9BF6ED860FF2@qq.sohu.com','domain':'.www.sogou.com','path':'/'})
driver.add_cookie({'name':'browerV', 'value':'2','domain':'.www.sogou.com','path':'/'})
driver.add_cookie({'name':'osV', 'value':'1','domain':'.www.sogou.com','path':'/'})

driver.add_cookie({'name':'FINSGFLAG', 'value':'true','domain':'.sogou.com','path':'/'})
driver.add_cookie({'name':'pgv_pvi', 'value':'4900557824','domain':'.sogou.com','path':'/'})
driver.add_cookie({'name':'pgv_si', 'value':'s3309892608','domain':'.sogou.com','path':'/'})
driver.add_cookie({'name':'sct', 'value':'8','domain':'.sogou.com','path':'/'})

driver.add_cookie({'name':'IPLOC', 'value':'CN1100','domain':'.sogou.com','path':'/'})
driver.add_cookie({'name':'ppinf', 'value':'5|1449821010|1451030610|Y2xpZW50aWQ6NDoyMDE3fGNydDoxMDoxNDQ5ODIxMDEwfHJlZm5pY2s6Mjc6JUU1JUE0JUE5JUU1JUEwJTgyJUU2JUIwJUI0fHRydXN0OjE6MXx1c2VyaWQ6NDQ6OTM2N0MxNEU0ODEwODdGQkQzMEQ5QkY2RUQ4NjBGRjJAcXEuc29odS5jb218dW5pcW5hbWU6Mjc6JUU1JUE0JUE5JUU1JUEwJTgyJUU2JUIwJUI0fA','domain':'.sogou.com','path':'/'})
driver.add_cookie({'name':'pprdig', 'value':'gxB-hBYK6vlTStqlrXTO7gL3g3Qt2M1F1zCI0YqOgbQMkoPSnvMYgtgz-3wcI2xstogkFLuJKDGfmv5ckUU3WGokrLAeHjQH9s1BwlJPU1nO7MbYpdOeWMzdKp5_6joRoF7bgPoU0GOeu_h2UYJzlWecB7g4I_2NAkH8tQTbkiw','domain':'.sogou.com','path':'/'})
driver.add_cookie({'name':'ld', 'value':'C0ZZVyllll2Qzo2JlllllVB$kCwlllllzkaQZkllllwllllljholl5@@@@@@@@@@','domain':'.sogou.com','path':'/'})
driver.add_cookie({'name':'LSTMV', 'value':'285,276','domain':'.sogou.com','path':'/'})
driver.add_cookie({'name':'LCLKINT', 'value':'23461','domain':'.sogou.com','path':'/'})
#driver.get('http://mp.weixin.qq.com/s?__biz=MjM5NTQ2NTUyMQ==&mid=401650066&idx=2&sn=7b80fad876be80d787d0bee68ff2073b&3rd=MzA3MDU4NTYzMw==&scene=6#rd')
driver.get('http://m.qikan.com')
result=driver.page_source
soup = BeautifulSoup(result)
print(soup.find(id="activity-name").string)
content=soup.find(id="page-content")
print(str(content))