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
        print(Jd[0]['id'])
        print(Jd[0]['op'])
    except Exception:
        pass
