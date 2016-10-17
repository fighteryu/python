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

  
