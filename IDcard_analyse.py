import pickle
'''
aa=open('data.pkl','rb')
a=pickle.load(aa)
sfzid=input('ID:')
if len(sfzid) != 18:
    print('err')
    
else:
    analyse()
'''  
def analyse():
    province=sfzid[0:6]
    birthday_year=sfzid[6:10]
    birthday_month=sfzid[10:12]
    birthday_day=sfzid[12:14]
    boy_girl=sfzid[16]
    print(a[province])
    print("%s年%s月%s日出生"%(birthday_year,birthday_month,birthday_day))
    if int(sfzid[16])%2==0:
        print("妹子")
    else:
        print("汉子")

def jiaoyan():
    list1=[sfzid[i] for i in range(17)]#取身份证前17位
    jqyz=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]#加权值
    j=[]
    for i in range(17):
        j.append(int(list1[i])*int(jqyz[i])) #计算加权乘积
    s=0
    print(j)
    for x in range(17):
        s+=int(j[x])#计算加权和
    print(s)
    #计算校验位
    t=s%11
    m=(12-t)%11
    print(m)
    #判断最后一位校验位是否和输入身份证号最后一位匹配
    if ord(sfzid[17])==88:#ord()将字符转换为ascii码
        print('输入身份证有效！')
        analyse()
    elif m==int(sfzid[17]):
        print('输入身份证有效！')
        analyse()
        
    else:
        print('身份证号码无效！')


aa=open('data.pkl','rb')
a=pickle.load(aa)
while True:
    sfzid=input('ID:')
    if len(sfzid) != 18:
        print('err')
    
    else:
        jiaoyan()
    

