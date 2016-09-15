'''
import urllib.request  
import urllib.parse  
import re  
import urllib.request,urllib.parse,http.cookiejar  
import time  
      
def getHtml(url):  
      
          
        cj=http.cookiejar.CookieJar()  
        opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))  
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'),('Cookie','4564564564564564565646540')]  
      
        urllib.request.install_opener(opener)  
          
        page = urllib.request.urlopen(url)  
        html = page.read()  
        return html  
    #print ( html)  
      
      
    #html = getHtml("http://weibo.com/")  
def getimg(html):  
        html = html.decode('utf-8')  
        reg='"screen_name":"(.*?)"'  
        imgre = re.compile(reg)  
        src=re.findall(imgre,html)  
        return src  
      
    #print ("",getimg(html))  
      
uid=['2808675432','3888405676','2628551531','2808587400']  
for a in list(uid):  
    print (getimg(getHtml("http://weibo.com/"+a)))  
      
      
    time.sleep(1)
'''

import urllib.request
import json
def getHtml(url):
    page=urllib.request.urlopen(url)
    html = page.read()
    return html
html= getHtml("http://www.baidu.com")
print (html)

