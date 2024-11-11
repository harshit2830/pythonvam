import numpy as np
import pandas as pd

#Top 10 employee fired in 1 miliion

myDataFrame = pd.DataFrame(data=np.arange(0,1000000).reshape(100000,10))
print(myDataFrame)
print(myDataFrame.tail(1))

#top 10 lowest paid employees add 500
myDataFrame = pd.DataFrame(data=np.arange(0,1000000).reshape(100000,10))
print(myDataFrame)
print(myDataFrame.head(1)+500)

#Average 100000 employees provide bonus of 100 for their increment
myDataFrame = pd.DataFrame(data=np.arange(0,1000000).reshape(100000,10))
print(myDataFrame)
print(myDataFrame.loc[[45000,55000]]+100)


myDataFrame = pd.DataFrame(data=np.arange(0,1000000).reshape(10,100000))
print(myDataFrame)
print(myDataFrame.loc[[5]]+100)

myData= np.arange(0,12)
dataFrame=pd.DataFrame(data=myData.reshape(3,4))
print(dataFrame)
print(dataFrame.iloc[1:3,1:3])

dataFrame.to_json("samplle.json")
dataFrame.to_csv("samplle.csv")
dataFrame.to_excel("samplle.xlsx")
