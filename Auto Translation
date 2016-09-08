'''
print ('-----')
temp = input ('caishuzi')
guess = int(temp)
if guess == 8:
    print('waaaaaa')
    print('so what')
else:
    print('err')
print ('go!')

pause
'''
'''
score = input('shurufenshu:  ')
dengji = int(score)
if 100>= dengji > 90:
    print('dengji:A')
elif 80<dengji<=90:
    print('dengji:B')
elif 80>= dengji > 60:
    print('dengji:C')
elif dengji<=60:
   print('dengji:D')
else:
    print('error')
'''
'''
a = 9
b = 10
c = 9 if a>b else 10

print (c)
'''
'''
#元组
tuple1 = ('aaa','bbb','ccc','ddd','eee')
tuple2 = tuple1[:2]+('hello',)+tuple1[2:]

#获取web
import urllib.request
respons = urllib.request.urlopen("http://www.baidu.com",timeout=1)
html = respons.read()
print (html)

#解码
html = html.decode('utf-8')
'''
'''
#downloadjpg

import urllib.request
respons = urllib.request.urlopen('http://placekitten.com/g/500/600')
cat_img = respons.read()

with open('cat.jpg','wb') as f:
    f.write(cat_img)
'''
'''
#获取链接地址
respons.geturl()
#获取http message 对象
respons.info()

respons.getcode()
'''

#Auto translation 
import urllib.request
import urllib.parse
import json

content = input('input:')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
data={}
data['type']='AUTO'
data['i']=content
data['doctype']='json'
data['xmlVersion']='1.8'
data['keyfrom']='fanyi.web'
data['ue']='UTF-8'
data['action']='FY_BY_CLICKBUTTON'
data['typoResult']='true'
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')
'''
target = json.loads(html)
print('output:%s'%(target['translateResult'][0][0]['tgt']))
'''
print(html)

from PIL import Image, ImageDraw, ImageFont

def add_num(picPath, num):
    img = Image.open(picPath)
    x, y = img.size
    myfont = ImageFont.truetype('Futura.ttf', x / 3)
    ImageDraw.Draw(img).text((2 * x / 3, 0), str(num), font = myfont, fill = 'red')
    img.save('pic_with_num.jpg')

if __name__ == '__main__':
    add_num('pic.jpg', 9)


import Image, ImageDraw, ImageFont, ImageFilter
import random

#random letter
def rndChar():
    return chr(random.randint(65, 90))

#random colour1
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

#random colour2
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

#240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
#Font object
font = ImageFont.truetype('Arial.ttf', 36)
#Draw object
draw = ImageDraw.Draw(image)
#draw
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
#output
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
#fuzzy
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg');


#born random char
import random
a = input('enter char number:')
for i in range(0,int(a)):
    chars = chr(random.randint(65,122))
    print('%s'%(chars),end = '')

'''
#words quantity
with open('test.txt', 'r') as f:
    from collections import Counter
    c = Counter()
    for line in f:
        words = line.split()
        # print(words)
        c += Counter(words)
    for words in c.most_common():
print(words)
'''
'''
#feidigui
def jiecheng(n):
    for i in range(1,n):
        n *= i
    return n
number = input('shurushuzi:')
number2 = int(number)
s = jiecheng(number2)
print('%d的阶乘是%d'%(number2,s))
'''
'''
#digui
def jiecheng(n):
    if n == 1:
        return 1
    else:
        return n*jiecheng(n-1)
number = input('shurushuzi:')
number2 = int(number)
s = jiecheng(number2)
print('%d的阶乘是%d'%(number2,s))
'''

'''
#菲波那契_递归算法
def feibnq(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return feibnq(n-1) + feibnq(n-2)
a = input('输入月数：')
number = int(a)
m = feibnq(number)
print('%d月兔子的数量是%d'%(number,m))
'''
'''
#菲波那契_迭代算法
def feibnq(n):
    n1 = 1
    n2 = 1
    n3 = 2
    while(n-2):
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1
    return n3

a = input('输入月数：')
number = int(a)
M = feibnq(number)
print('%d月兔子的数量是%d'%(number,M))
'''

#Hanoi
def hanoi(n,A,B,C):
    if n == 1:
        print(A,'--->',C)
    else:
        hanoi(n-1,A,C,B)
        print(A,'--->',C)
        hanoi(n-1,B,A,C)
n = int(input('盘子数量？'))
hanoi(n,'A','B','C')

#打包便于大数据调用
#demo
import pickle
name = ['123','abc','222','345',['8','9']]
pickle_t = open('name_data.aaa','wb')
pickle.dump(name,pickle_t)
pickle_t.close()
pickle_t_1 = open('name_data.aaa','rb')
c = pickle.load(pickle_t_1) 







    
    
