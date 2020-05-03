#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import os
import openpyxl
import matplotlib.pyplot as plt
import itertools


# In[3]:


## reading data
balance = pd.read_excel(open('Баланс-2020-05-02-3.xlsx', 'rb'), sheet_name='Движ')
balance.drop(['Планир. расх', 'Планир. дох','Unnamed: 14','Unnamed: 15','Unnamed: 16'],axis=1,inplace=True)
balance.rename(columns={'Дата':'Date','Раздел':'Section','Организация':'Who','Расх':'Expences','Дох':'Income','ИТОГО':'TOTAL','Категория':'Category','Подкатег':'Subcat','Подкат2':'Subcat2','Коммент':'Comment','Месяц/ Год':'Month','Банк':'Bank'},inplace=True)
balance = balance.loc[balance['Date']<='2020-04-30']

# In[4]:


bal2020 = balance.loc[balance['Date']>='2020-01-01']
life = bal2020.loc[bal2020['Section'] == 'Life']
jan = life.loc[life.Expences>0].loc[life['Month'] =='2020-1'].groupby('Category').sum()['Expences']
feb = life.loc[life.Expences>0].loc[life['Month'] =='2020-2'].groupby('Category').sum()['Expences']
march = life.loc[life.Expences>0].loc[life['Month'] =='2020-3'].groupby('Category').sum()['Expences']
aprl = life.loc[life.Expences>0].loc[life['Month'] =='2020-4'].groupby('Category').sum()['Expences']


# In[5]:


s6 =  balance.loc[(balance.Section=='S6') & (balance['Subcat']!='Залог') & (balance['Subcat']!='СФ')]
s6_aunt = balance.loc[(balance.Category=='Тетя Саша') & (balance['Subcat']!='Ремонт')]
# calculation S6-our revenue
table = pd.pivot_table(s6_aunt, values=['Expences','Income','TOTAL'],
                       index=['Month', 'Category'],
                       columns=[],
                       fill_value=0, aggfunc=np.sum, dropna=True, )
aunt_pivot = pd.concat([
    d.append(d.sum().rename((k, 'Total')))
    for k, d in table.groupby(level=0)
]).append(table.sum().rename(('Grand', 'Total')))

# calculation S6-aunt's revenue
table = pd.pivot_table(s6, values=['Expences','Income','TOTAL'],
                       index=['Month', 'Category','Subcat'],
                       columns=[],
                       fill_value=0, aggfunc=np.sum, dropna=True, )
s6_pivot = pd.concat([
    d.append(d.sum().rename((k, 'Total')))
    for k, d in table.groupby(level=0)
]).append(table.sum().rename(('Grand', 'Total')))
print("Aunt's revenue for S6 (reversed minus)")
print(aunt_pivot.tail(9))
print('')
print('')
print('Our revenue for S6')
print(s6_pivot.tail(23))


# In[12]:


bal2020_edit = bal2020.loc[bal2020.Subcat != 'Залог']
exp = bal2020_edit.loc[bal2020.Expences>0]
income = bal2020_edit.loc[bal2020.Income>0]
## all income and expences
inc_area = bal2020_edit[['Month','Expences','Income']].groupby(['Month']).sum()
inc_area.plot(kind='line',figsize=(20,10), fontsize=14,marker='*')
plt.grid(True, linestyle='--')
plt.legend(fontsize=14)
plt.title('Lines with income and expences (data without prepayments)', fontsize=16)
plt.savefig('Lines with income and expences.pdf')
## split income and expences on sections
inc_table = pd.pivot_table(bal2020_edit, values=['Income'],
                       index=['Month'],
                       columns=['Section'],
                       fill_value=0, aggfunc=np.sum, dropna=True, )
exp_table = pd.pivot_table(bal2020_edit, values=['Expences'],
                       index=['Month'],
                       columns=['Section'],
                       fill_value=0, aggfunc=np.sum, dropna=True, )
tot_table = pd.pivot_table(bal2020_edit, values=['Expences','Income'],
                       index=['Month'],
                       columns=['Section'],
                       fill_value=0, aggfunc=np.sum, dropna=True, )

fig = plt.figure(figsize=(20,8))
ax0 = fig.add_subplot(121)
ax1 = fig.add_subplot(122,sharey=ax0)
# bar with income
inc_table.plot(kind='bar',ax=ax0, fontsize=16)
ax0.grid(True, linestyle='--')
ax0.legend(fontsize=14)
ax0.set_title('Income', fontsize=16)
# bar with expences
exp_table.plot(kind='bar',ax=ax1, fontsize=16)
ax1.grid(True, linestyle='--')
ax1.legend(fontsize=14)
ax1.set_title('Expences', fontsize=16)

plt.tight_layout()
plt.savefig('Income and expences subcats wise.pdf')
## bar with all exp and income
tot_table.plot(kind='bar',figsize=(20,10), fontsize=16)
plt.title('Bars with income and expences subcats wise (data without prepayments)', fontsize=16)
plt.grid(True)
plt.legend(fontsize=16)
plt.savefig('Bars with income and expences subcats wise.pdf')
# plt.show()
# plt.savefig('Bars with income and expences subcats wise (data without prepayments).pdf')


# In[13]:


# plt.style.use('ggplot')

## function for labeling with values - autopct=make_autopct(values)
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}% ({v:d})'.format(p=pct,v=val)
    return my_autopct

#### Pie charts with Life data
fig, ax = plt.subplots(2,2, figsize=(15, 15))
### January
## Pie chart with grouping together all elements whose value is less than 2000rub
dic = jan.sort_values(ascending=False).to_dict()
newdic={}
# grouping small elements in one group
for key, group in itertools.groupby(dic, lambda k: 'Остальное' if dic[k]<=2000 else k):
    newdic[key] = sum((dic[k] for k in list(group)))

ax[0, 0].pie(newdic.values(), labels=newdic.keys(), autopct=make_autopct(newdic.values()), startangle=0, shadow=True)
ax[0, 0].set_title("January "+str(int(jan.sum()))+" rub.", fontsize=14)

### February|
## Pie chart with grouping together all elements whose value is less than 2000rub
dic = feb.sort_values(ascending=False).to_dict()
newdic={}
# grouping small elements in one group
for key, group in itertools.groupby(dic, lambda k: 'Остальное' if (dic[k]<=2000) else k):    
    newdic[key] = sum([dic[k] for k in list(group)])

ax[0, 1].pie(newdic.values(),labels=newdic.keys(), autopct=make_autopct(newdic.values()), startangle=0, shadow=True)
ax[0, 1].set_title("February "+str(int(feb.sum()))+" rub.", fontsize=14)

### March
## Pie chart with grouping together all elements whose value is less than 2000rub
dic = march.sort_values().to_dict()
newdic={}
# grouping small elements in one group
for key, group in itertools.groupby(dic, lambda k: 'Остальное' if (dic[k]<=2000) else k):
    newdic[key] = sum([dic[k] for k in list(group)])

ax[1, 0].pie(newdic.values(), labels=newdic.keys(), autopct=make_autopct(newdic.values()), startangle=0, shadow=True)
ax[1, 0].set_title("March "+str(int(march.sum()))+" rub.", fontsize=14)

### April
## Pie chart with grouping together all elements whose value is less than 2000rub
dic = aprl.sort_values(ascending=False).to_dict()
newdic={}
# grouping small elements in one group
for key, group in itertools.groupby(dic, lambda k: 'Остальное' if (dic[k]<=2000) else k):
    newdic[key] = sum([dic[k] for k in list(group)])

ax[1, 1].pie(newdic.values(),labels=newdic.keys(), autopct=make_autopct(newdic.values()), startangle=0, shadow=True)
ax[1, 1].set_title("April "+str(int(aprl.sum()))+" rub.", fontsize=14)
plt.savefig('Life expences category wise (pies).pdf')
# plt.show()


# In[8]:


### Bar charts with Life data
# make new dfs to add rows that doesn't exist in the month but exist in all period
list = life.loc[life.Expences>0]['Category'].unique() # category list of expences that was in the period
new_df = pd.DataFrame(index=list)
new_jan = pd.concat([new_df,jan]).reset_index().groupby('index').sum().rename(columns={0: 'January'})
new_feb = pd.concat([new_df,feb]).reset_index().groupby('index').sum().rename(columns={0: 'February'})
new_march = pd.concat([new_df,march]).reset_index().groupby('index').sum().rename(columns={0: 'March'})
new_aprl = pd.concat([new_df,aprl]).reset_index().groupby('index').sum().rename(columns={0: 'April'})
# make consolidated df
all_m = pd.DataFrame(index=new_jan.index)
all_m['January'] = new_jan.values
all_m['February'] = new_feb.values
all_m['March'] = new_march.values
all_m['April'] = new_aprl.values
all_m.reset_index(inplace=True)
# plot bars
all_m.plot(x='index', y=['January', 'February','March','April'], kind="bar",figsize=(20,10))
plt.legend(fontsize=16)
plt.grid()
plt.title('Life expences', fontsize=16)
plt.xticks(rotation=90,fontsize=12)
plt.savefig('Life expences category wise (bars).pdf')
# plt.show()


# In[14]:


### Horizontal bar charts
fig, ax = plt.subplots(2,2,figsize=(15,10),sharey='row',sharex='col')

ax[0,0].barh(new_jan.index,new_jan.values.flatten(),)
ax[0,0].set_title('January life expences')
ax[0,0].grid(axis='both', linestyle='--')

ax[1,0].barh(new_jan.index,new_feb.values.flatten())
ax[1,0].set_title('February life expences')
ax[1,0].grid(axis='both', linestyle='--')

ax[0,1].barh(new_jan.index,new_march.values.flatten())
ax[0,1].set_title('March life expences')
ax[0,1].grid(axis='both', linestyle='--')

ax[1,1].barh(new_jan.index,new_aprl.values.flatten())
ax[1,1].set_title('April life expences')
ax[1,1].grid(axis='both', linestyle='--')

plt.tight_layout()
plt.savefig('Life expences category wise(horizontal bars).pdf')
# plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




