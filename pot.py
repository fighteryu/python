# No.1
class A:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def S(self):
    return self.x * self.y
  def C(self):
    return 2*self.x +2*self.y
    
a = A(3,4)
s = a.S()
c = a.C()
print(s,c)

#No.2
class A:
  def S(self,x,y):
    return x * y
  def C(self,x,y):
    return 2*x +2*y
    
a = A()
s = a.S(3,4)
c = a.C(3,4)
print(s,c)

####回忆下面这段
def nextnum(num):
    temp = '0'
    result = ''
    counter = 0
    str_num = str(num)
    for ch in str_num:
        if ch != temp:
            result += str(counter)
            result += temp
            temp = ch
            counter = 1
        else:
            counter += 1
    result += str(counter)
    result += temp
    return int(result)
lst = [1] 
for x in xrange(0,30):
    lst.append(nextnum(lst[x]))
print(len(str(lst[30])))

#3
import time as t
class clock():
    def __init__(self):
        self.unit = ['y','m','d','h','mi','s']
        self.prompt = 'no beginning'
        self.lasted = []
        self.begin = 0
        self.end = 0
    def __str__(self):
        return self.prompt
    
    __repr__ = __str__
    def start(self):
        print('start....')
        self.begin = t.localtime()
    def stop(self):
        self.end = t.localtime()
        self._calc()
        print('stop!')
    def _calc(self):
        self.lasted = []
        self.prompt =  'lasted:'
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
            
#4
class A:
  #定义该类的属性被访问时的行为
  def __getattribute__(self,name): 
    print('getattribute')
    return super().__getattribute__(name)
  #定义用户获取一个不存在的属性时的行为
  def __getattr__(self,name):
    print('getattr')
  #定义当一个属性被设置时的行为
  def __setattr__(self,name,value):
    print('setattr')
    super().__setattr__(name,value)
  #定义一个属性被删除时的行为
  def __delattr__(self,name):
    print('delattr')
    super().__delattr__(name)

class rectangle:
  def __init__(self,width=0,height=0):
    self.width = width
    self.height = height
  def __setattr__(self,name,value):
    if name == 'square':
      self.width = value
      self.height = value
    else:
      super().__setattr__(name,value)
  def area(self):
      return self.width * self.height
    
class a:
	def __get__(self,instance,owner):
		print('getting...',self,instance,owner)
	def __set__(self,instance,value):
		print('setting...',self,instance,value)
	def __delete__(self,instance):
		print('delete...',self,instance)

#5 Xpath
import urllib.request
import scrapy
from lxml import etree
html=urllib.request.urlopen("http://www.2345.com")
response=html.read()
selecter=etree.HTML(response)
pipid=selecter.xpath("//ul[@class='cont-list']//li/a/text()")
for i in range(0,len(pipid)):
    print(pipid[i])

#6 JD价格Json数据
import urllib.request
from lxml import etree
import json
for i in range(1111111,10000000):
    try:
        url='https://p.3.cn/prices/mgets?&skuIds=J_'+str(i)
        response=urllib.request.urlopen(url)
        response2=response.read().decode('utf-8')
	#json.load用于将原先str数据类型转化为list数据类型
        Jd=json.loads(response2)
        with open("list.txt","a") as f:
            f.write(Jd[0]['id'])
            f.write("\t")
            f.write(Jd[0]['op'])
            f.write("\n")
    except Exception:
        print('err....')
	
#使用代理，以防止IP被封或IP次数受限：
proxy_handler = urllib.request.ProxyHandler(proxies={"http": "1.1.1.1:8080"})

opener = urllib.request.build_opener(proxy_handler)     # 利用代理创建opener实例
response = opener.open(url)                             # 直接利用opener实例打开url

urllib.request.install_opener(opener)                   # 安装全局opener，然后利用urlopen打开url
response = urllib.request.urlopen(url)


# 使用cookie和cookiejar,应对服务器检查
cookie_jar = http.cookiejar.CookieJar()
cookie_jar_handler = urllib.request.HTTPCookieProcessor(cookiejar=cookie_jar)
opener = urllib.request.build_opener(cookie_jar_handler)
response = opener.open(url)


# 发送在浏览器中获取的cookie,两种方式:
# (1)直接放到headers里
headers = {
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
    "Cookie": "PHPSESSID=btqkg9amjrtoeev8coq0m78396; USERINFO=n6nxTHTY%2BJA39z6CpNB4eKN8f0KsYLjAQTwPe%2BhLHLruEbjaeh4ulhWAS5RysUM%2B; "
}
request = urllib.request.Request(url, headers=headers)

# (2)构建cookie,添加到cookiejar中
cookie = http.cookiejar.Cookie(name="xx", value="xx", domain="xx", ...)
cookie_jar.set_cookie(cookie)
response = opener.open(url)


# 同时使用代理和cookiejar
opener = urllib.request.build_opener(cookie_jar_handler)
opener.add_handler(proxy_handler)
response = opener.open("https://www.baidu.com/")


# 抓取网页中的图片：同样适用于抓取网络上的文件。右击鼠标，找到图片属性中的地址，然后进行保存。
response = urllib.request.urlopen("http://ww3.sinaimg.cn/large/7d742c99tw1ee7dac2766j204q04qmxq.jpg", timeout=120)
with open("test.jpg", "wb") as file_img:
    file_img.write(response.read())


# HTTP认证：即HTTP身份验证
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()     # 创建一个PasswordMgr
password_mgr.add_password(realm=None, uri=url, user='username', passwd='password')   # 添加用户名和密码
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)         # 创建HTTPBasicAuthHandler
opener = urllib.request.build_opener(handler)                       # 创建opner
response = opener.open(url, timeout=10)                             # 获取数据


#邮件轰炸,如何隐藏发送者地址？
import yagmail
import time
import random
while 1:
    if random.randint(3,100)%3==0:
        a=time.localtime()
        try:
            m=yagmail.SMTP(user='sendemailadd',password='password',host='smtp.sina.com',port='25')
            m.send(to='sendtomailadd',subject='this is a test mail by yagmail',contents=str(a))
            print('邮件发送成功！')
        except  Exception as e:
            print('邮件未送达')
    else:
        print('pass')
	
#requests方法，登录科学网，貌似保存了cookie了
#面对复杂的网页会自动调整cookie，所以此方法无效，需要用到requests的session函数
'''
session=requests.Session()
s=session.post(url,data)
s=session.get(url)
'''
import requests
import urllib.request
import urllib.parse
class science:
    def __init__(self):
        self.url='http://blog.sciencenet.cn/member.php?mod=logging&action=login2&loginsubmit=yes&infloat=yes'
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        self.data={'username':'username',
                   'password':'password',
                   'kxwpassword':'password',
                   'quickforward':'yes',
                   'handlekey':'ls',
                   'iflogin':'plus.php?mod=iframelogin'}
        self.postdata=urllib.parse.urlencode(self.data).encode('utf-8')
    def login(self):
        '''
        response=urllib.request.Request(self.url,self.postdata,self.headers)
        html=urllib.request.urlopen(response)
        '''
        response=requests.post(self.url,self.postdata,self.headers)
        cookies=response.cookies#获取到当前cookie
        response2=requests.get(self.url,cookies)#将cookie再发送回页面
        page=response2.text
        print(page)
	
a=science()
a.login()


#读取数据库，并写入csv文件
import pymssql
import csv
conn=pymssql.connect('127.0.0.1','username','keyword','databasename')
curs=conn.cursor()
curs.execute('select * from *******')
with open('data.csv','a',newline='') as f:#newline=''这个不写会出现插入一条数据就空一行数据现象
    writer=csv.writer(f)
    writer.writerow(['id','data'])
    for row in curs:
        data=[row[2],row[3]]
        writer.writerow(data)
conn.close()

#电脑打卡上下班
import pymssql
import time
conn=pymssql.connect('127.0.0.1','sa','sa','test')
cursor=conn.cursor()
idd=input('请输入你的工号：')
timer=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
try:
    sql='INSERT INTO userinfo VALUES (%s,%d,%d,%s,%s,%d,%s)'
    cursor.execute(sql,(1,idd,12,'dd','ss',5,timer))
    print('机器打卡成功！')
except:
    print('error')

conn.commit()#commit一定需要，如果没有无法插入数据，但是仍然占据一条自增ID
conn.close()

#数据可视化demo
import numpy as num
import pandas as pd
import matplotlib.pylab as pyl
import pymysql
conn=pymysql.connect(host='',user='',passwd='',db='')
sql='select * from ××××××'
data=pd.read_sql(sql,conn)
data1=data.T   #数据转置后方便提取整列的数据
a=data1.values[3]
b=data1.values[4]
pyl.plot(a,b,'o')# 'o'是绘制散点图，a，b表示横纵轴
pyl.show()#显示图像


#闲鱼年会奖品转卖
import urllib
import urllib.request
import csv
import time
from lxml import etree

def xianyu():
    for i in range(2,100):
        user_agent='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        url='https://s.2.taobao.com/list/list.htm?&page='+str(i)+'&q=%C4%EA%BB%E1%BD%B1%C6%B7'
        html=urllib.request.urlopen(url)
        page=html.read()
        data=etree.HTML(page)
        title=data.xpath("//h4[@class='item-title']//a/text()")
        price=data.xpath("//div[@class='item-price price-block']//span/em/text()")
        '''
        with open('xianyu.csv','a',newline='') as f:
            writer=csv.writer(f)
            writer.writerow(['name','price'])
            data1=[title,price]
            writer.writerows(data1)
            f.close()
        '''
        print('目前正在爬取第'+str(i)+'页')
        for j in range(len(title)):
            
            with open('xianyu.txt','a') as f:
                f.write(title[j])
                f.write('\n')
                f.write(price[j])
                f.write('\n')
                f.write('-------------------------\n')

        time.sleep(5)

if __name__=='__main__':
    xianyu()


#获取闲鱼总页码
pagenum=data1.xpath("//span[@class='paginator-count']/text()")
pagenum1=str(pagenum[0])
pagenum2=pagenum1[1:4]#获取‘共100页’字符串中的100


#微信红包随机问题
'''
只是整数，取m-1个断点，将金额分成m份，取间隔即是金额
'''
import random
a=input('输入总金额：')
b=input('输入红包个数：')

def hongbao(money,m):
    #list1=[float('%.2f'%random.uniform(1,money)) for x in  range(m)]
    list1=[random.randint(1,money-1) for x in range(m-1)]
    list1.sort()
    list2=[]
    print(list1)
    sum1=0
    for i in range(m-1):
        if i==0:
            a=list1[i]
            print(a)  
        else:
            b=list1[i]-list1[i-1]
            print(b)
    c=money-list1[m-2]
    print(c)
        
hongbao(int(a),int(b))


#jieba模块验证红楼梦前八十回和后四十回相似度
'''
前四十回与后四十回相似21.023819%  中间四十回与后四十回相似度25.171706%
你说这算不算一个作者写的？？？
'''
import jieba
from gensim import corpora,models,similarities
from collections import defaultdict
data1=open('c:\\Users\\Administrator\\Desktop\\hlm1.txt','r',encoding='utf-8').read()
data2=open('c:\\Users\\Administrator\\Desktop\\hlm3.txt','r',encoding='utf-8').read()
a=jieba.cut(data1)
b=jieba.cut(data2)
data11=""
for i in a:
    data11+=i+" "

data22=""
for i in b:
    data22+=i+" "

documents=[data11,data22]
texts=[[word for word in document.split()] for document in documents]
frequency=defaultdict(int)
for text in texts:
    for token in text:
        frequency[token]+=1
#print(frequency)

dictionary=corpora.Dictionary(texts)
dictionary.save('dict2.txt')

data3=open('c:\\Users\\Administrator\\Desktop\\hlm2.txt','r',encoding='utf-8').read()
c=jieba.cut(data3)
data33=""
for i in c:
    data33+=i+" "

data333=data33
#print(data333)
#建立向量
vec1=dictionary.doc2bow(data333.split())
#print(vec1)
corpus=[dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('data333.mm',corpus)

tfidf=models.TfidfModel(corpus)
featureNum=len(dictionary.token2id.keys())
#print(featureNum)
index=similarities.SparseMatrixSimilarity(tfidf[corpus],num_features=featureNum)
sim=index[tfidf[vec1]]
#print(tfidf[vec1])
print(sim)


#冒泡排序按字母顺序排序
a="OkhaoPingCeilXu"
b=[a[i] for i in range(len(a))]
for i in range(len(b)):
	for j in range(i+1,len(b)):
		if ord(b[i])<96:
			b[i],b[j]=b[j],b[i]
c=""
for i in range(len(b)):
        c+=b[i]

print(c)#输出khaoingeiluXCPO


#知乎

import http.cookiejar
import urllib.request
import urllib.parse

class zhihu():
    def __init__(self):
        self.url='https://www.zhihu.com/login/email'
        self.headers={"Host":"www.zhihu.com",
                     "User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:47.0) Gecko/20100101 Firefox/47.0",
                     "Accept":"*/*",
                     "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                     "Accept-Encoding":"gzip, deflate, br",
                     "X-Xsrftoken":"d85ac3db1867cb416cb45df4990cc8c5",
                     "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                     "X-Requested-With":"XMLHttpRequest",
                     "Referer":"https://www.zhihu.com/",
                     "Content-Length":"83",
                     "Cookie":"********",
                     "Connection":"keep-alive"}
        self.data={"_xsrf":"×××××××××",
                   "password":"××××××××××",
                   "email":"××××××××××××"}
        self.postdata=urllib.parse.urlencode(self.data).encode('utf-8')

    
    def login(self):
        #No.1
        '''
        response=urllib.request.Request(self.url,self.postdata,self.headers)
        response1=urllib.request.urlopen(response,timeout=10)
        html=response1.read().decode('utf-8')
        print(html)
        '''
        #No.2
        #filename='cookie.txt'
        #cookie_jar=http.cookiejar.MozillaCookieJar(filename)
        cookie_jar=http.cookiejar.CookieJar()
        cookie_jar_handle=urllib.request.HTTPCookieProcessor(cookie_jar)
        opener=urllib.request.build_opener(cookie_jar_handle)
        response=opener.open(self.url,self.postdata)
        html=response.read().decode('utf-8')
        print(html)
        #cookie_jar.save(ignore_discard=True, ignore_expires=True)
    
    def spider(self):
        url='https://www.zhihu.com/topics'
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:47.0) Gecko/20100101 Firefox/47.0",
                 "Cookie":"*****************************"}
        response=urllib.request.Request(url,headers=headers)
        response1=urllib.request.urlopen(response,timeout=10)
        html=response1.read().decode('utf-8')
        print(html)
       
a=zhihu()
a.login()
a.spider()
    
