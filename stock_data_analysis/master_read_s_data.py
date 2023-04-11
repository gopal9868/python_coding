import pandas as pd
import datetime
import requests
from datetime import datetime
from pytz import timezone
from bs4 import BeautifulSoup
tz = timezone('EST')
now = datetime.now(tz)
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
if len(str(now.month))==1:
   month='0'+str(now.month)
else:
   month = str(now.month)
if len(str(now.day))==1:
   day='0'+str(now.day)
else:
   day = str(now.day)
if len(str(now.hour))==1:
   hour='0'+str(now.hour)
else:
   hour = str(now.hour)
if len(str(now.minute))==1:
   minute='0'+str(now.minute)
else:
   minute = str(now.minute)
dt1=str(now.year)+month+day+hour+minute
with open ('C:/Project/s_data/master_list.csv','r') as f1:
 for line in f1:
  s_cd=line.strip()
  price = 0
  #print(s_cd)
  url='https://finance.yahoo.com/quote/'+s_cd+'?p='+s_cd+'&.tsrc=fin-srch'
  response=''
  response=requests.get(url,headers = headers)
  soup = BeautifulSoup(response.text, 'lxml')
  price = soup.find("fin-streamer", {"data-symbol":s_cd,"data-field":"regularMarketPrice"}).text
  #print(soup.prettify())
  with open('C:/Project/s_data/master_s_output.csv','a') as f2:
     f2.write(s_cd+','+str(price)+','+dt1+'\n')

