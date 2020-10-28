"""
plot covid data that defined in csv file data_minimal.csv.
"""
import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("./data/united_states_covid19_cases_and_deaths_by_state.csv")
data.columns

data1 = data.loc[data['Total Cases']>10000]

x = data1['State']
y = data1['Total Cases']
y1 = data1['Total Deaths']

plt.plot(x,y, x, y1)


plt.legend(loc=1)
plt.show()