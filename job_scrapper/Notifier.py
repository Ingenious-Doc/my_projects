from threading import main_thread
from bs4 import BeautifulSoup
from pandas.core.reshape import encoding
import requests
import math
import pandas as pd
l=[]
url="https://www.linkedin.com/jobs/search/?currentJobId=3700217888&distance=25&f_E=2&geoId=104305776&keywords=software%20engineer&origin=JOBS_HOME_SEARCH_CARDS"
response=requests.get(url)
souper=BeautifulSoup(response.text,'html.parser')
jb=souper.find('title')
number=""
for i in jb.text:
    try:
        number+=str(int(i))
        
    except:
        break
url+="&start={}"
number_of_jobs=math.ceil(int(number)/25)
for i in range(0,number_of_jobs):
    res=requests.get(url.format(i))
    soup=BeautifulSoup(res.text,'html.parser')
    all_jobs_on_this_page=soup.find_all('li')
    for x in range(0,len(all_jobs_on_this_page)):
        if all_jobs_on_this_page[x].find('div',{"class":"base-card"}):
            jobid=all_jobs_on_this_page[x].find('div',{"class":"base-card"}).get('data-entity-urn').split(":")[3]
            l.append(jobid)
target_url='https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'
k=[]
print(len(l))
for j in range(0,len(l)):
    o={}
    resp=requests.get(target_url.format(l[j]))
    soup=BeautifulSoup(resp.text,'html.parser')
    try:
        o["company"]=soup.find("div",{"class":"top-card-layout__card"}).find('a').find('img').get('alt')
    except:
        o['company']=None
    try:
        o['job-title']=soup.find("div",{'class':'top-card-layout__entity-info'}).find('a').text.strip()
    except:
        o['job-title']=None
    try:
        o['level']=soup.find('div',{"class":"description__job-criteria-list"}).find('li').text.replace("Seniority level","").strip()
    except:
        o['level']=None
    k.append(o)
    
df=pd.DataFrame(k)
df.to_csv('linkinJobs.csv',index=False,encoding='utf-8')