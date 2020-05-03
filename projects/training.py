## Pie chart with grouping together all elements whose value is less than 2000rub
dic = feb.sort_values(ascending=False).to_dict()
newdic={}
# grouping small elements in one group
for key, group in itertools.groupby(dic, lambda k: 'Остальное' if (dic[k]<=2000) else k):
    newdic[key] = sum([dic[k] for k in list(group)])

labels = newdic.keys()
sizes = newdic.values()

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct=make_autopct(sizes), startangle=0, shadow=True)
ax.axis('equal')
ax.set_title("February "+str(int(feb.sum()))+" rub.", fontsize=14)
plt.tight_layout()
plt.show()

## Pie chart with grouping together all elements whose value is less than 2000rub
dic = march.sort_values().to_dict()
newdic={}
# grouping small elements in one group
for key, group in itertools.groupby(dic, lambda k: 'Остальное' if (dic[k]<=2000) else k):
    newdic[key] = sum([dic[k] for k in list(group)])

labels = newdic.keys()
sizes = newdic.values()

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct=make_autopct(sizes), startangle=0, shadow=True)
ax.axis('equal')
ax.set_title("March "+str(int(march.sum()))+" rub.", fontsize=14)
plt.tight_layout()
plt.show()


## Pie chart with grouping together all elements whose value is less than 2000rub
dic = aprl.sort_values(ascending=False).to_dict()
newdic={}
# grouping small elements in one group
for key, group in itertools.groupby(dic, lambda k: 'Остальное' if (dic[k]<=2000) else k):
    newdic[key] = sum([dic[k] for k in list(group)])

labels = newdic.keys()
sizes = newdic.values()

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct=make_autopct(sizes), startangle=0, shadow=True)
ax.axis('equal')
ax.set_title("April: "+str(int(aprl.sum()))+" rub.", fontsize=14)
plt.tight_layout()
plt.show()