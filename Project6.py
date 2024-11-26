# 2023: $30.4 billion
# 2022: -$2.7 billion (loss)
# 2021: $33.4 billion
# 2020: $21.3 billion
# 2019: $11.6 billion
# 2018: $10.1 billion
# 2017: $3.0 billion
# 2016: $2.4 billion
# 2015: $0.6 billion
# 2014: -$0.2 billion (loss)

from sklearn.metrics import r2_score
import numpy as np
import matplotlib.pyplot as plt

year = [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014]
#Revenue in billions of dollars 
Revenue = [30.4, -2.7, 33.4, 21.3, 11.6, 10.1, 3.0, 2.4, 0.6, -0.2] 
# plt.scatter(age, salary, marker = 'o')
# plt.show()
futureRevenue = np.poly1d(np.polyfit(year, Revenue, 3))
print(futureRevenue(2025))
print(r2_score(Revenue, futureRevenue(year)))