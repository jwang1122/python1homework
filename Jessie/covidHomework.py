"""
parse covid-19 data US_NY vs US_TX Confirmed
    - [Online data](https://open-covid-19.github.io/data/data_minimal.csv)
"""
import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# keep US_MO data
date1 = []
missouriConfirmed = []
missouriDeath = []
# keep US_TX data
date2 = []
texasConfirmed = []
texasDeath = []
#  keep US_CO
date3 = []
coloradoConfirmed = []
coloradoDeath = []

first = True
with open('./data/data_minimal1.csv', 'r') as covid_19:
#    reader = csv.reader(covid_19)
    for row in covid_19:
#        print(row)
        if first:
            first = False
            continue
        line = row.split(',')
        if (line[1]=='US_MO'):
            date1.append(datetime.strptime(line[0], '%Y-%m-%d'))
            confirmed = int(line[2])
            missouriConfirmed.append(confirmed)
            death = line[3].strip()
            death = int(death) if len(death)>0 else 0
            missouriDeath.append(int(death))
        if(line[1] == 'US_TX'):
            date2.append(datetime.strptime(line[0], '%Y-%m-%d'))
            confirmed = int(line[2])
            texasConfirmed.append(confirmed)
            death=line[3].strip()
            death = int(death) if len(death)>0 else 0
            texasDeath.append(death)
        if (line[1]=='US_CO'):
            date3.append(datetime.strptime(line[0], '%Y-%m-%d'))
            confirmed = int(line[2])
            coloradoConfirmed.append(confirmed)
            death=line[3].strip()
            death = int(death) if len(death)>0 else 0
            coloradoDeath.append(death)

    
    covid_19.close()

#print(date1)
#print(misouriConfirmed)
# print(len(date2))
fig=plt.figure()

x = date1
y = missouriConfirmed
z = missouriDeath

ax=fig.add_subplot(1,2,1)
ax.plot(x,y,c='y',ls='-.',label='Missouri')
ax.plot(date2,texasConfirmed,c='b',ls='-',label='Texas')
ax.plot(date3,coloradoConfirmed,c='r',ls=':',label='Colorado')
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlabel='Date', ylabel='Confirmed',
       title='Covid-19 Confirmed Report')
plt.legend(loc=2)

ax2=fig.add_subplot(1,2,2)
ax2.plot(x,z,c='y', ls='-.',label='Missouri')
ax2.plot(date2,texasDeath,c='b',ls='-',label='Texas')
ax2.plot(date3,coloradoDeath,c='r',ls=':',label='Colorado')
labels2 = ax2.get_xticklabels()
plt.setp(labels2, rotation=45, horizontalalignment='right')
ax2.set(xlabel='Date', ylabel='Death',
       title='Covid-19 Death Report')

ax.locator_params(axis='y', nbins=7)
plt.legend(loc=2)
plt.show()
