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
  
