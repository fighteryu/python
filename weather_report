import urllib.request
import json
import pickle
import os
import sys
sys.path.append(r'C:\Python34\Lib\site-packages')

def current_file_directory():
    import os, sys, inspect
    path = os.path.realpath(sys.path[0])        # interpreter starter's path
    if os.path.isfile(path):                    # starter is excutable file
        path = os.path.dirname(path)
        return os.path.abspath(path)            # return excutable file's directory
    else:                                       # starter is python script
        caller_file = inspect.stack()[1][1]     # function caller's filename
        return os.path.abspath(os.path.dirname(caller_file))# return function caller's

#city_data pickle
#pkl_city = {'city_name':'city_code',............}
pkl_city = open("{path}\\city.pkl".format(path=current_file_directory()),"rb")
city = pickle.load(pkl_city)
pkl_city.close()

city_name = input('请输入城市名:')
password = city.get(city_name)
#url_file_name = 'http://m.weather.com.cn/data/{password}.html'.format(password=password)
#url_file = urllib.request.urlopen(url_file_name)
#weatherHTML = url_file.read().decode('utf-8')
#weatherJSON = json.JSONDecoder().decode(weatherHTML)
#weatherInfo = weatherJSON['weatherinfo']

#print('城市：', weatherInfo.get('city'))
#print('时间：', weatherInfo.get('date_y'),weatherInfo.get('week'))
#period=range(1,7)
#for no in period:
# print('-'*50)
# hour=no*24
# print('{hour}小时天气：'.format(hour=hour))
# print('温度：', weatherInfo.get('temp{no}'.format(no=no)))
# print('天气：', weatherInfo.get('weather{no}'.format(no=no)))
# print('风速：', weatherInfo.get('wind{no}'.format(no=no)))

# if no == 1:
# hour=""
# index_d = "index{hour}_d".format(hour=hour)
# if index_d in weatherInfo.keys():
# print('穿衣指数：', weatherInfo.get(index_d))

# index_uv = "index{hour}_uv".format(hour=hour)
# if index_uv in weatherInfo.keys():
# print('紫外线：', weatherInfo.get(index_uv))

url_file_name = 'http://www.weather.com.cn/data/sk/{password}.html'.format(password=password)
url_file = urllib.request.urlopen(url_file_name)
weatherHTML = url_file.read().decode('utf-8')
weatherJSON = json.JSONDecoder().decode(weatherHTML)
weatherInfo = weatherJSON['weatherinfo']

url_file_name = 'http://www.weather.com.cn/data/cityinfo/{password}.html'.format(password=password)
url_file = urllib.request.urlopen(url_file_name)
weatherHTML = url_file.read().decode('utf-8')
weatherJSON = json.JSONDecoder().decode(weatherHTML)
weatherInfo2 = weatherJSON['weatherinfo']
#http://m.weather.com.cn/img/ 图片地址
print('城市：', weatherInfo.get('city'))
print('播报时间：', weatherInfo.get('time'))
print('-'*50)
print('天气：', weatherInfo2.get('weather'),weatherInfo2.get('img1'),weatherInfo2.get('img2'))
print('室外温度：%s℃' % (weatherInfo.get('temp')))
print('温度：%s-%s' % (weatherInfo2.get('temp2'),weatherInfo2.get('temp1')))
print('风力：', weatherInfo.get('WD'), weatherInfo.get('WS'))
