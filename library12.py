import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# NOTE: in line,bar,scatters,graph the dataset must be of same lenght 

years = np.array([2020,2021,2022,2024])
grades = np.array([90.8,88,87,78])

#show data in line graph- line(x,y),pie(y),
#bar(x,y), scatters(x,y)

plt.plot(years, grades,marker = 'o')
#give the graph title
plt.title("Academic Growth")
#set the  x and y axis
plt.xlabel("Years")
plt.ylabel("Grades")
plt.show()

trendinglangName = np.array(['python','javascript','java','c#'])
trendingLang = np.array(['45','30','20','5'])
plt.title("trending language marketplace")
plt.pie(trendingLang)
plt.legend(trendinglangName)
plt.show()

#jio 5 years sell growth,2020-2024
jioSellyear = np.array([2020,2021,2022,2023,2024])
jiosales = np.array([100,120,150,180,200])
plt.bar(jioSellyear,jiosales)
plt.title("Jio Sell Growth")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.show()

