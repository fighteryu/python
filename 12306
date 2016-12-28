import urllib.request
import json
import yagmail as m
import time
date=input('请输入乘车日期：')
fromstation=input('请输入起始站代号：')
tostation=input('请输入终到站代号：')
bbbb=input('请输入订阅的车次：')
purpose_codes='ADULT'
url='https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date='+date+'&leftTicketDTO.from_station='+fromstation+'&leftTicketDTO.to_station='+tostation+'&purpose_codes='+purpose_codes
html=urllib.request.urlopen(url)
response=html.read().decode('utf-8')
urldata=json.loads(response)
for i in range(0,len(urldata['data'])):
    #获取火车车票信息    
    if urldata['data'][i]['queryLeftNewDTO']['station_train_code']==bbbb:
        startstation=urldata['data'][i]['queryLeftNewDTO']['start_station_name']
        endstation=urldata['data'][i]['queryLeftNewDTO']['end_station_name']
        traincode=urldata['data'][i]['queryLeftNewDTO']['station_train_code']
        yw=urldata['data'][i]['queryLeftNewDTO']['yw_num']#硬卧
        rw=urldata['data'][i]['queryLeftNewDTO']['rw_num']#软卧
        gr=urldata['data'][i]['queryLeftNewDTO']['gr_num']#高级软卧
        zy=urldata['data'][i]['queryLeftNewDTO']['zy_num']#一等座
        ze=urldata['data'][i]['queryLeftNewDTO']['ze_num']#二等座
        tz=urldata['data'][i]['queryLeftNewDTO']['tz_num']#特等座
        #gg=urldata['data'][i]['queryLeftNewDTO']['gg_num']#
        #yb=urldata['data'][i]['queryLeftNewDTO']['yb_num']#
        wz=urldata['data'][i]['queryLeftNewDTO']['wz_num']#无座
        qt=urldata['data'][i]['queryLeftNewDTO']['qt_num']#其他
        swz=urldata['data'][i]['queryLeftNewDTO']['swz_num']#商务座
        yz=urldata['data'][i]['queryLeftNewDTO']['yz_num']#硬座
        rz=urldata['data'][i]['queryLeftNewDTO']['rz_num']#软座
        try:
            if ze!='--' and ze!='无':
                s=m.SMTP(user='******',password='******',host='*******',port='25')
                b=time.asctime()
                s.send(to='********@gmail.com',subject='车次信息from12306',contents='尊敬的主人，截至'+str(b)+','+str(traincode)+'次列车已经有票，请抓紧到12306网站购买，错过就真的错过了！因邮件延时，说不定等你点开的时候就已经卖完喽，快点哦')
                print('邮件发送成功！')
            else:
                pass
        except Exception as e:
            print('邮件发送失败')     
    else:
        pass
    
    

