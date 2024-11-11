import numpy as np
import  pandas as pd

#create an array start from 0 to 49
#empsalary = np.array([0,1,2,3,4])
empsalary  = np.arange(10)
print(empsalary)

#find the min.max,mean from empsalary

print("Mean is",empsalary.mean())
print("Max is",empsalary.max())
print("Min is",empsalary.min())
myData = empsalary.reshape(2,5)
mydata = myData+500
print(myData)
print(myData>505)
print("shape is ",myData.shape)
print(myData)

#Array slicing
print(empsalary[:])
emp = ([5,6,3,2,1,9,10,4,7,8])
print(emp[ : -5])

#pandas will represent the dataset in dataframes
myDataFrame = pd.DataFrame(data=np.arange(0,50).reshape(5,10))
print(myDataFrame)
print("mean",myDataFrame.mean())
print("median",myDataFrame.median())
print("mode",myDataFrame.mode())
print(myDataFrame.head(1))
print(myDataFrame.tail())
print(myDataFrame.locp[[6,]])



