import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import datetime
import pandas as pd
from pandasql import sqldf
import numpy as np
df = pd.read_csv("C:/Project/s_data/master_s_output.csv")
df['PrevPrice'] = df.groupby('Stock')['Price'].shift(1)
df["rank"] = df.groupby(['Stock'])['Date'].rank(method='dense',ascending=False).astype(int)
#print(df[['Stock','Price','PrevPrice','rank']])
df['change_pct']=((df["Price"]-df["PrevPrice"])*100)/df["PrevPrice"]
#print(df)
q="""select Stock, max(case when rank=1 then Price else null end) Price1,
max(case when rank=1 then change_pct else null end) Change_Pct1,
coalesce(max(case when rank=1 then Price else null end),0) Price2,
coalesce(max(case when rank=2 then change_pct else null end),0) Change_Pct2,
max(case when rank=3 then Price else null end) Price3,
max(case when rank=3 then change_pct else null end) Change_Pct3,
max(case when rank=4 then Price else null end) Price4,
max(case when rank=4 then change_pct else null end) Change_Pct4,
max(case when rank=5 then Price else null end) Price5,
max(case when rank=5 then change_pct else null end) Change_Pct5,
max(case when rank=6 then Price else null end) Price6,
max(case when rank=6 then change_pct else null end) Change_Pct6,
max(case when rank=7 then Price else null end) Price7,
max(case when rank=7 then change_pct else null end) Change_Pct7,
max(case when rank=8 then Price else null end) Price8,
max(case when rank=8 then change_pct else null end) Change_Pct8,
max(case when rank=9 then Price else null end) Price9,
max(case when rank=9 then change_pct else null end) Change_Pct9,
max(case when rank=10 then Price else null end) Price10,
max(case when rank=10 then change_pct else null end) Change_Pct10,
max(case when rank=11 then Price else null end) Price11,
max(case when rank=11 then change_pct else null end) Change_Pct11,
max(case when rank=12 then Price else null end) Price12,
max(case when rank=12 then change_pct else null end) Change_Pct12,
max(case when rank=13 then Price else null end) Price13,
max(case when rank=13 then change_pct else null end) Change_Pct13,
max(case when rank=14 then Price else null end) Price14,
max(case when rank=14 then change_pct else null end) Change_Pct14,
max(case when rank=15 then Price else null end) Price15,
max(case when rank=15 then change_pct else null end) Change_Pct15
from df group by Stock"""
newdf=sqldf(q,globals())
newdf=np.round(newdf, decimals=2)
newdf=newdf.fillna(0)
i=1
x=newdf['Stock']
st=0
bottomval=0
while i<16:
    colname='Change_Pct'+str(i)
    newcolname='change_pct'+str(i)+'_color'
    conditions=[(newdf[colname]>0),(newdf[colname]<=0)]
    values=['green','red']
    newdf[newcolname]=np.select(conditions,values)
    t = abs(newdf[colname])
    lablename='t'+str(i)
    if i==1:
     plt.bar(x, t, label=lablename, color=newdf[newcolname], edgecolor='black')
    else:
     plt.bar(x, t, bottom=bottomval, label=lablename, color=newdf[newcolname], edgecolor='black')

    i=i+1
    bottomval = t + bottomval
#print(newdf[['Stock','Change_Pct1','Change_Pct2','Change_Pct3','change_pct2_color']])
#plt.bar(x,t3,0.3,bottom=t2+t1,label='t3',color=newdf['change_pct3_color'],edgecolor='black')
plt.xlabel("Stock")
plt.ylabel("Change %")
plt.show()
