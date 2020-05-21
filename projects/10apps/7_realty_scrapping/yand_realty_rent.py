#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests, re
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime as dt


# In[2]:


url = 'https://realty.yandex.ru/sankt-peterburg/snyat/kvartira/studiya/metro-devyatkino/?metroTransport=ON_FOOT&timeToMetro=10&sort=DATE_DESC'
url_to_pages=url+'&page='
site='https://'+url.split('/')[2]

soup=BeautifulSoup(requests.get(url).content,"html.parser")
page_numb=int(int(soup.find("div",{"FormField_name_submit"}).text.split(' ')[1])/20)


# In[54]:


apartm_list=[]
for page in range(0,int(page_numb/4)):
    soup=BeautifulSoup(requests.get(url_to_pages+str(page)).content,"html.parser")
    data=soup.find_all("ol",{"OffersSerp__list"})[0].find_all('li',{'OffersSerpItem'})
    print(page) # to track if there would be an error
    for item in data:
        apartm_dict={}
        link=site+item.find('a',{'OffersSerpItem__link'}, href=True)['href']
        new_soup=BeautifulSoup(requests.get(link).content,"html.parser").find_all('div',{'Offer'})[0]
        build=item.find_all('div',{'OffersSerpItem__building'})[0].text.split(', ')
        print(build) # to track if there would be an error
        
        apartm_dict['title']=item.find('h3',{'OffersSerpItem__title'}).text     
        apartm_dict['zhk']=build[0]
        try:
            apartm_dict['layer']=build[1]
        except:
            if 'этаж' in build[0]:
                apartm_dict['layer']=build[0]
                apartm_dict['zhk']=None
            else:
                apartm_dict['layer']=None
        apartm_dict['address']=item.find('div',{'OffersSerpItem__address'}).text
        try:
            fees=new_soup.find('span',{'OfferDealDescription__info-item'}).text
            if "комисси" in fees: 
                apartm_dict['fees']=fees
            else:
                apartm_dict['fees']=None  
        except:
            apartm_dict['fees']=None
        apartm_dict['location']=item.find('span',{'MetroWithTime__body'}).text[10:-5]
        apartm_dict['price']=item.find('span',{'price'}).text
        try:
            apartm_dict['desc']=item.find('p',{'OffersSerpItem__description'}).text
        except:    
            apartm_dict['desc']=None
        try:
            apartm_dict['full_desc']=new_soup.find('p',{'OfferTextDescription__text'}).text
        except:    
            apartm_dict['full_desc']=None
        try:
            apartm_dict['date']=new_soup.find('div',{'OfferPublishedDate'}).text
        except:
            apartm_dict['date']=item.find('div',{'OffersSerpItem__publish-date'}).text
        try:
            apartm_dict['update_date']=apartm_dict['date'].split('(')[1][10:-1]
        except:
            apartm_dict['update_date']=apartm_dict['date']
        apartm_dict['link']=link
        apartm_list.append(apartm_dict)

df=pd.DataFrame(apartm_list)
df.to_excel("first.xlsx")


# In[55]:


apartm_list=[]
for page in range(int(page_numb/4),int(page_numb/2)):
    soup=BeautifulSoup(requests.get(url_to_pages+str(page)).content,"html.parser")
    data=soup.find_all("ol",{"OffersSerp__list"})[0].find_all('li',{'OffersSerpItem'})
    print(page) # to track if there would be an error
    for item in data:
        apartm_dict={}
        link=site+item.find('a',{'OffersSerpItem__link'}, href=True)['href']
        new_soup=BeautifulSoup(requests.get(link).content,"html.parser").find_all('div',{'Offer'})[0]
        build=item.find_all('div',{'OffersSerpItem__building'})[0].text.split(', ')
        print(build) # to track if there would be an error
        
        apartm_dict['title']=item.find('h3',{'OffersSerpItem__title'}).text     
        apartm_dict['zhk']=build[0]
        try:
            apartm_dict['layer']=build[1]
        except:
            if 'этаж' in build[0]:
                apartm_dict['layer']=build[0]
                apartm_dict['zhk']=None
            else:
                apartm_dict['layer']=None
        apartm_dict['address']=item.find('div',{'OffersSerpItem__address'}).text
        try:
            fees=new_soup.find('span',{'OfferDealDescription__info-item'}).text
            if "комисси" in fees: 
                apartm_dict['fees']=fees
            else:
                apartm_dict['fees']=None  
        except:
            apartm_dict['fees']=None
        apartm_dict['location']=item.find('span',{'MetroWithTime__body'}).text[10:-5]
        apartm_dict['price']=item.find('span',{'price'}).text
        try:
            apartm_dict['desc']=item.find('p',{'OffersSerpItem__description'}).text
        except:    
            apartm_dict['desc']=None
        try:
            apartm_dict['full_desc']=new_soup.find('p',{'OfferTextDescription__text'}).text
        except:    
            apartm_dict['full_desc']=None
        try:
            apartm_dict['date']=new_soup.find('div',{'OfferPublishedDate'}).text
        except:
            apartm_dict['date']=item.find('div',{'OffersSerpItem__publish-date'}).text
        try:
            apartm_dict['update_date']=apartm_dict['date'].split('(')[1][10:-1]
        except:
            apartm_dict['update_date']=apartm_dict['date']
        apartm_dict['link']=link
        apartm_list.append(apartm_dict)

df=pd.DataFrame(apartm_list)
df.to_excel("second.xlsx")
result=pd.concat([pd.read_excel("rent_"+str(dt.now())[:11]+".xlsx"), df]).reset_index(drop=True)
result.to_excel("rent_"+str(dt.now())[:11]+".xlsx")


# In[56]:


apartm_list=[]
for page in range(int(page_numb/2),int(page_numb*3/4)):
    soup=BeautifulSoup(requests.get(url_to_pages+str(page)).content,"html.parser")
    data=soup.find_all("ol",{"OffersSerp__list"})[0].find_all('li',{'OffersSerpItem'})
    print(page) # to track if there would be an error
    for item in data:
        apartm_dict={}
        link=site+item.find('a',{'OffersSerpItem__link'}, href=True)['href']
        new_soup=BeautifulSoup(requests.get(link).content,"html.parser").find_all('div',{'Offer'})[0]
        build=item.find_all('div',{'OffersSerpItem__building'})[0].text.split(', ')
        print(build) # to track if there would be an error
        
        apartm_dict['title']=item.find('h3',{'OffersSerpItem__title'}).text     
        apartm_dict['zhk']=build[0]
        try:
            apartm_dict['layer']=build[1]
        except:
            if 'этаж' in build[0]:
                apartm_dict['layer']=build[0]
                apartm_dict['zhk']=None
            else:
                apartm_dict['layer']=None
        apartm_dict['address']=item.find('div',{'OffersSerpItem__address'}).text
        try:
            fees=new_soup.find('span',{'OfferDealDescription__info-item'}).text
            if "комисси" in fees: 
                apartm_dict['fees']=fees
            else:
                apartm_dict['fees']=None  
        except:
            apartm_dict['fees']=None
        apartm_dict['location']=item.find('span',{'MetroWithTime__body'}).text[10:-5]
        apartm_dict['price']=item.find('span',{'price'}).text
        try:
            apartm_dict['desc']=item.find('p',{'OffersSerpItem__description'}).text
        except:    
            apartm_dict['desc']=None
        try:
            apartm_dict['full_desc']=new_soup.find('p',{'OfferTextDescription__text'}).text
        except:    
            apartm_dict['full_desc']=None
        try:
            apartm_dict['date']=new_soup.find('div',{'OfferPublishedDate'}).text
        except:
            apartm_dict['date']=item.find('div',{'OffersSerpItem__publish-date'}).text
        try:
            apartm_dict['update_date']=apartm_dict['date'].split('(')[1][10:-1]
        except:
            apartm_dict['update_date']=apartm_dict['date']
        apartm_dict['link']=link
        apartm_list.append(apartm_dict)

df=pd.DataFrame(apartm_list)
df.to_excel("third.xlsx")
result=pd.concat([pd.read_excel("rent_"+str(dt.now())[:11]+".xlsx"), df]).reset_index(drop=True)
result.to_excel("rent_"+str(dt.now())[:11]+".xlsx")


# In[4]:


apartm_list=[]
for page in range(int(page_numb*3/4),page_numb+1):
    soup=BeautifulSoup(requests.get(url_to_pages+str(page)).content,"html.parser")
    data=soup.find_all("ol",{"OffersSerp__list"})[0].find_all('li',{'OffersSerpItem'})
    print(page) # to track if there would be an error
    for item in data:
        apartm_dict={}
        link=site+item.find('a',{'OffersSerpItem__link'}, href=True)['href']
        new_soup=BeautifulSoup(requests.get(link).content,"html.parser").find_all('div',{'Offer'})[0]
        build=item.find_all('div',{'OffersSerpItem__building'})[0].text.split(', ')
        print(build) # to track if there would be an error
        
        apartm_dict['title']=item.find('h3',{'OffersSerpItem__title'}).text     
        apartm_dict['zhk']=build[0]
        try:
            apartm_dict['layer']=build[1]
        except:
            if 'этаж' in build[0]:
                apartm_dict['layer']=build[0]
                apartm_dict['zhk']=None
            else:
                apartm_dict['layer']=None
        apartm_dict['address']=item.find('div',{'OffersSerpItem__address'}).text
        try:
            fees=new_soup.find('span',{'OfferDealDescription__info-item'}).text
            if "комисси" in fees: 
                apartm_dict['fees']=fees
            else:
                apartm_dict['fees']=None  
        except:
            apartm_dict['fees']=None
        apartm_dict['location']=item.find('span',{'MetroWithTime__body'}).text[10:-5]
        apartm_dict['price']=item.find('span',{'price'}).text
        try:
            apartm_dict['desc']=item.find('p',{'OffersSerpItem__description'}).text
        except:    
            apartm_dict['desc']=None
        try:
            apartm_dict['full_desc']=new_soup.find('p',{'OfferTextDescription__text'}).text
        except:    
            apartm_dict['full_desc']=None
        try:
            apartm_dict['date']=new_soup.find('div',{'OfferPublishedDate'}).text
        except:
            apartm_dict['date']=item.find('div',{'OffersSerpItem__publish-date'}).text
        try:
            apartm_dict['update_date']=apartm_dict['date'].split('(')[1][10:-1]
        except:
            apartm_dict['update_date']=apartm_dict['date']
        apartm_dict['link']=link
        apartm_list.append(apartm_dict)

df=pd.DataFrame(apartm_list)
df.to_excel("fourth.xlsx")
result=pd.concat([pd.read_excel("rent_"+str(dt.now())[:11]+".xlsx"), df]).reset_index(drop=True)
result.to_excel("rent_"+str(dt.now())[:11]+".xlsx")
result.drop(['Unnamed: 0','Unnamed: 0.1.1','Unnamed: 0.1.1.1','level_0','index']], axis=1, inplace=True)
result.to_excel("rent_"+str(dt.now())[:11]+".xlsx")


# In[9]:


result=pd.concat([pd.read_excel("rent_"+str(dt.now())[:11]+".xlsx"), df]).reset_index(drop=True)
def metro(loc): return 'Close' if loc<=11 else 'Far'
result['metro']=[metro(loc) for loc in result.location]
result.drop(['Unnamed: 0','Unnamed: 0.1.1','Unnamed: 0.1.1.1','level_0','index'], axis=1, inplace=True)
result.drop_duplicates(keep=first, inplace=True)
result.to_excel("rent_"+str(dt.now())[:11]+".xlsx")


# In[53]:


result=pd.concat([pd.read_excel("first.xlsx"), pd.read_excel("second.xlsx"), pd.read_excel("third.xlsx"), pd.read_excel("fourth.xlsx")]).reset_index(drop=True)
result.drop(['Unnamed: 0'], axis=1, inplace=True)
def metro(loc): return 'Close' if loc<=11 else 'Far'
result['metro']=[metro(loc) for loc in result.location]
result.drop_duplicates(keep=first, inplace=True)
result.to_excel("rent_v2_"+str(dt.now())[:11]+".xlsx")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




