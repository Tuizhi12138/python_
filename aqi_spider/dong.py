import numpy as np
import pandas as pd

#读取数据
aqi=pd.read_excel('all_aqi.xlsx')
patient=pd.read_excel('PM2.5 入院出院日期.xlsx')

#将日期格式更改为日期字符串
aqi['日期']=aqi['日期'].astype(str)
patient['入院日期']=patient['入院日期'].astype(str)
patient['出院日期']=patient['出院日期'].astype(str)

#求出各病人住院期间的PM2.5均值并写入patient表格中
pm_mean = []
for i in patient.index:
    start1 = patient.iloc[i][1]
    stop1 = patient.iloc[i][2]
    avg1 = aqi.loc[(aqi['日期']>=start1)&(aqi['日期']<=stop1),'PM2.5'].mean()
    pm_mean.append(avg1)
patient['PM_2.5_mean']=pm_mean

#保存
patient.to_excel('result.xlsx',index=False)