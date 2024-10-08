#list in python
#list stores multiple data
mylist= ["pawan","ivan","dev"]
#tuple stores multiple data
mytuple=("pawan","ivan","dev")
#set store multiple data
myset={"pawan","ivan","dev"}
#dictionary store multiple data in key value pair
myDict={"name":"pawan","email":"p@gmail.com"}

#to check the data types of all above data set
print("list:",type(mylist),"tuple:",type(mytuple))
print("set:",type(myset),"dict",type(myDict))

#how to identify list,set,tuple,dictionary
# list -> [], tuple -> (), set ->{}  , dictionary -> {:}

#example of data set
mydata={"pawan","deepanshu","mahi"}
mygroup=("pawan","deepanshu","mahi")
myclass=["pawan","deepanshu","mahi"]
myfriends={"name":"pawan","age":33}

#orignal name of data set
mySet={"pawan","deepanshu","mahi"}
myTuple=("pawan","deepanshu","mahi")
myList=["pawan","deepanshu","mahi"]
myDict={"name":"pawan","age":33}

#access specific data from data set
print("lsit:",myList[0] )
print("tuple :",myTuple[0],"dict :",myDict["name"])

#access complete data from data set
for data in myList:
    print("list",data)
for item in mySet:
    print("set",item)
for value in myTuple:
    print("tuple",value)
for x in myDict.values():
    print("dict",x)       

#to check which data set support duplicate data
print("list",myList,"tuple",myTuple,"dict",myDict,"set",mySet)

#to update the data in all data set
myList[0]="tripti"
print(myList)

myDict[0]="tripti"
print(myDict)

# mySet[0]="tripti"
# print(mySet)

# myTuple[0]="tripti"
# print(myTuple)

#tuple and set is unchangeable 
#dictionary and list in changeable
#list ,tuple duplicate item
#set ,dictionary no duplicate item

#Add new value in data set
myList.append("saloni")
mySet.add("Saloni")
myDict.update({"name":"Saloni"})
print("list",myList,"tuple",myTuple,"dict",myDict,
        "set",mySet)

#to remove  data from data set
myDict.pop("name")
myList.pop(0)
mySet.remove("pawan")
print("list",myList,
      "tuple",myTuple,"dict",myDict,
        "set",mySet)

#convert tuple to list
convertList=list(mytuple)
print (type(convertList))

convertList.append("rohan")
convertList.pop(2)
print(convertList)
myTuple = tuple(convertList)
print(myTuple)

