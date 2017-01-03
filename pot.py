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
s=session.post(url,postdata)
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
