import pandas as pd
from pandasql import sqldf
import smtplib
from read_s_data_vol import get_stock_data
get_stock_data()
def email_alert(stock,change_pct):
    user="gopstockalert@gmail.com"
    password="bqktmahptfsnblpd"
    recipient = 'gopstockalert@gmail.com'
    subject=text="Volume of Stock "+stock+' has gone up to '+str(change_pct)
    text=subject
    message = 'Subject: {}\n\n{}'.format(subject , text)
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.sendmail(user, recipient, message)
    server.quit()
df = pd.read_csv("C:/Project/s_data/s_vol_output.csv")
df['Volume'] = df['Volume'].astype('float')
df['PrevVolume'] = df.groupby('Stock')['Volume'].shift(1)
df["rank"] = df.groupby(['Stock'])['Date'].rank(method='dense',ascending=False).astype(int)
q=""" select Stock,Currentvol,Prevvol1,Prevvol2,
 case when Prevvol1=0 and Prevvol2=0 then 0 when Prevvol1>0 
and Prevvol2=0 then ((Currentvol-Prevvol1)-(Prevvol1))/(Prevvol1)*100
when  Prevvol1<>0 and Prevvol2<>0
then ((Currentvol-Prevvol1)-(Prevvol1-Prevvol2))/(Prevvol1-Prevvol2)*100 else 0 end change_pct from 
(select Stock, max(case when rank=1 then Volume else 1 end) Currentvol,
max(case when rank=2 then Volume else 0 end) Prevvol1,
max(case when rank=3 then Volume else 0 end) Prevvol2 from df where rank in (1,2,3) group by Stock) a
"""
newdf=sqldf(q,globals())
#print(newdf)
latestdf=newdf.loc[(newdf['change_pct'] >300.0)]
if len(latestdf.index)>0:
    for index, row in latestdf.iterrows():
        stock=row['Stock']
        chg_pct=int(row['change_pct'])
        email_alert(stock,chg_pct)


