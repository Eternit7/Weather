import json
import sys
import requests

weatherPlace = input("请输入城市名称:")
if weatherPlace == 'E' or weatherPlace =='e':
    sys.exit()
#天气数据地址
weatherJsonUrl = "http://wthrcdn.etouch.cn/weather_mini?city=%s"%(weatherPlace)
#向服务器发送天气查询请求
response = requests.get(weatherJsonUrl)
try:
    response.raise_for_status()
except:
    print('网址请求错误!')

weatherData = json.loads(response.text)
#print(weatherData)
w = weatherData['data']
print("城市：%s"%w['city'])
#存放五天天气信息
weather = []
#五天天气的高温
highTemp = []
#五天天气的低温
lowTemp = []
#日期
date = []
for i in range(len(w['forecast'])):
    date.append(w['forecast'][i]['date'])
    weather.append(w['forecast'][i]['type'])
    highTemp.append(w['forecast'][i]['high'])
    lowTemp.append(w['forecast'][i]['low'])
    print('日期:%s'%date[i])
    print('温度:最%s ~最%s'%(lowTemp[i],highTemp[i]))
    print('天气:%s'%weather[i])
print('穿衣提示:%s'%w['ganmao'])
print('当前温度:%s'%w['wendu'])
