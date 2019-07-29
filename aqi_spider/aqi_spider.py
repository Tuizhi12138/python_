#导入环境
from selenium import webdriver
import time
import re
import numpy as np
import pandas as pd

#获取全部北京数据信息
url0='https://www.aqistudy.cn/historydata/monthdata.php?city=%E5%8C%97%E4%BA%AC'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url0)
time.sleep(10)
pattern=re.compile(r'href="(daydata.php.+?city=北京.+?month=[0-9]+?)"')
pic_list = re.findall(pattern,driver.page_source)

#抓取所有的数据并存入list中
result_list=[]
for m in pic_list:
    url = 'https://www.aqistudy.cn/historydata/{}'.format(m)
    url = url.replace('amp;', '')
    driver.get(url)
    time.sleep(30)

    # 提取网页中的表格信息
    pattern_ = re.compile(r'">(.+?)</td>')
    element = re.findall(pattern_, driver.page_source)
    pattern_2 = re.compile(r'<span.+?>(.+?)</span>')
    d_list = []

    for i in range(len(element)):
        if len(element[i]) == 103 or len(element[i]) == 106:
            linshi = re.findall(pattern_2, element[i])
            #         print(linshi[0])
            element[i] = linshi[0]
        elif len(element[i]) <= 10:
            pass
        else:
            element[i] = ''
            d_list.append(i)

    while True:
        try:
            del element[d_list[0]]
        except:
            break
    result_list.append(element)

driver.close()#关闭窗口

#放入dataframe中并保存，方便后期使用
columns=['日期','AQI','质量等级','PM2.5','PM10','SO2','CO','NO2','O3_8h']
all_aqi=pd.DataFrame(columns=columns)
for i in result_list:
    a=np.array(i)
    a=a.reshape(int((len(i)/9)),9)
    all_aqi=all_aqi.append(pd.DataFrame(a,columns=columns),ignore_index = True)

all_aqi.to_excel('all_aqi.xlsx',index=False,encoding='utf-8')