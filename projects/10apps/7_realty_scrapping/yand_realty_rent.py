#!/usr/bin/env python
# coding: utf-8

# In[43]:


import requests, re
from bs4 import BeautifulSoup
import pandas as pd


# In[44]:


url = 'https://realty.yandex.ru/sankt-peterburg/snyat/kvartira/studiya/metro-devyatkino/?metroTransport=ON_FOOT&timeToMetro=10&sort=DATE_DESC'
url_to_pages=url+'&page='
site='https://'+url.split('/')[2]

soup=BeautifulSoup(requests.get(url).content,"html.parser")
page_numb=int(int(soup.find("div",{"FormField_name_submit"}).text.split(' ')[1])/20)


# In[46]:


apartm_list=[]
for page in range(0,int(page_numb/4)+1):
    soup=BeautifulSoup(requests.get(url_to_pages+str(page)).content,"html.parser")
    data=soup.find_all("ol",{"OffersSerp__list"})[0].find_all('li',{'OffersSerpItem'})
    print(page) # to track if there would be an error
    for item in data:
        apartm_dict={}
        link=site+item.find('a',{'OffersSerpItem__link'}, href=True)['href']
        new_soup=BeautifulSoup(requests.get(link).content,"html.parser").find_all('div',{'Offer'})[0]
        build=item.find_all('div',{'OffersSerpItem__building'})[0].text.split(', ')
        print(build[0]+' '+build[1]) # to track if there would be an error
        
        apartm_dict['title']=item.find('h3',{'OffersSerpItem__title'}).text     
        apartm_dict['zhk']=build[0]
        apartm_dict['layer']=build[1]
        apartm_dict['address']=item.find('div',{'OffersSerpItem__address'}).text
        try:
            fees=new_soup.find('span',{'OfferDealDescription__info-item'}).text
            if "комисси" in fees: 
                apartm_dict['fees']=fees
            else:
                apartm_dict['fees']=None  
        except:
            apartm_dict['fees']=None
        apartm_dict['location']=item.find('span',{'MetroWithTime__body'}).text[10:]
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


# In[ ]:


apartm_list=[]
for page in range(int(page_numb/4),int(page_numb/2)+1):
    soup=BeautifulSoup(requests.get(url_to_pages+str(page)).content,"html.parser")
    data=soup.find_all("ol",{"OffersSerp__list"})[0].find_all('li',{'OffersSerpItem'})
    print(page) # to track if there would be an error
    for item in data[:10]:
        apartm_dict={}
        link=site+item.find('a',{'OffersSerpItem__link'}, href=True)['href']
        new_soup=BeautifulSoup(requests.get(link).content,"html.parser").find_all('div',{'Offer'})[0]
        build=item.find_all('div',{'OffersSerpItem__building'})[0].text.split(', ')
        print(build[0]+' '+build[1]) # to track if there would be an error
        
        apartm_dict['title']=item.find('h3',{'OffersSerpItem__title'}).text     
        apartm_dict['zhk']=build[0]
        apartm_dict['layer']=build[1]
        apartm_dict['address']=item.find('div',{'OffersSerpItem__address'}).text
        try:
            fees=new_soup.find('span',{'OfferDealDescription__info-item'}).text
            if "комисси" in fees: 
                apartm_dict['fees']=fees
            else:
                apartm_dict['fees']=None  
        except:
            apartm_dict['fees']=None
        apartm_dict['location']=item.find('span',{'MetroWithTime__body'}).text[10:]
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
result=pd.concat([pd.read_excel("first.xlsx"), df]).reset_index()
result.to_excel("rent.xlsx")


# In[ ]:


apartm_list=[]
for page in range(int(page_numb/2),int(page_numb*3/4)+1):
    soup=BeautifulSoup(requests.get(url_to_pages+str(page)).content,"html.parser")
    data=soup.find_all("ol",{"OffersSerp__list"})[0].find_all('li',{'OffersSerpItem'})
    print(page) # to track if there would be an error
    for item in data[:10]:
        apartm_dict={}
        link=site+item.find('a',{'OffersSerpItem__link'}, href=True)['href']
        new_soup=BeautifulSoup(requests.get(link).content,"html.parser").find_all('div',{'Offer'})[0]
        build=item.find_all('div',{'OffersSerpItem__building'})[0].text.split(', ')
        print(build[0]+' '+build[1]) # to track if there would be an error
        
        apartm_dict['title']=item.find('h3',{'OffersSerpItem__title'}).text     
        apartm_dict['zhk']=build[0]
        apartm_dict['layer']=build[1]
        apartm_dict['address']=item.find('div',{'OffersSerpItem__address'}).text
        try:
            fees=new_soup.find('span',{'OfferDealDescription__info-item'}).text
            if "комисси" in fees: 
                apartm_dict['fees']=fees
            else:
                apartm_dict['fees']=None  
        except:
            apartm_dict['fees']=None
        apartm_dict['location']=item.find('span',{'MetroWithTime__body'}).text[10:]
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
result=pd.concat([pd.read_excel("rent.xlsx"), df]).reset_index()
result.to_excel("rent.xlsx")


# In[ ]:


apartm_list=[]
for page in range(int(page_numb*3/4),page_numb+1):
    soup=BeautifulSoup(requests.get(url_to_pages+str(page)).content,"html.parser")
    data=soup.find_all("ol",{"OffersSerp__list"})[0].find_all('li',{'OffersSerpItem'})
    print(page) # to track if there would be an error
    for item in data[:10]:
        apartm_dict={}
        link=site+item.find('a',{'OffersSerpItem__link'}, href=True)['href']
        new_soup=BeautifulSoup(requests.get(link).content,"html.parser").find_all('div',{'Offer'})[0]
        build=item.find_all('div',{'OffersSerpItem__building'})[0].text.split(', ')
        print(build[0]+' '+build[1]) # to track if there would be an error
        
        apartm_dict['title']=item.find('h3',{'OffersSerpItem__title'}).text     
        apartm_dict['zhk']=build[0]
        apartm_dict['layer']=build[1]
        apartm_dict['address']=item.find('div',{'OffersSerpItem__address'}).text
        try:
            fees=new_soup.find('span',{'OfferDealDescription__info-item'}).text
            if "комисси" in fees: 
                apartm_dict['fees']=fees
            else:
                apartm_dict['fees']=None  
        except:
            apartm_dict['fees']=None
        apartm_dict['location']=item.find('span',{'MetroWithTime__body'}).text[10:]
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
result=pd.concat([pd.read_excel("rent.xlsx"), df]).reset_index()
result.to_excel("rent.xlsx")


# In[ ]:


result=pd.concat([pd.read_excel("first.xlsx"), pd.read_excel("second.xlsx"), pd.read_excel("third.xlsx"), pd.read_excel("fourth.xlsx")]).reset_index()
result.to_excel("rent.xlsx")


# In[42]:


result=pd.concat([pd.read_excel("rent_dev1.xlsx"), pd.read_excel("rent_dev2.xlsx")]).reset_index()
result.to_excel("rent.xlsx")


# In[ ]:




