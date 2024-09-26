#Loist can store multiple data, data can be of different types like int,str,float
#list can store the duplicate data
#List is an ordered data set -- sorting it can ascending or descending


#create list and store the name of your friends

friendlist = ["Rahul", "Harshit", "jeet", "dev"]

#print the list of friend names\
print(friendlist)

#Add the age of your friends into list
#append is used to add the data into end of the list 
friendlist.append(36)
friendlist.append(26)
friendlist.append(29)
friendlist.append(5)
print(friendlist)

#ADD the data into list using index no
friendlist.insert(0,"nikss")
print(friendlist)

#to access the  data from list we use index no
print(friendlist[0])

#access the complete list
for name in friendlist:
    print(name)

#To remove data from the list
friendlist.remove("Harshit")     #remove data using value
print(friendlist)


#pop will delete data using index
friendlist.pop(2)                #remove data using index no.
print(friendlist)

#Add the 5 fav city name in the list
#Add my fav city name kasol in first index
#remove the last city name from list - using pop
#sorting the list data
   #friendlist.sort()
#print the list data

placelist =["Shimla","himachal","Chandigarh","Haryana","noida"]
placelist.insert(0,"kasol")
placelist.pop(4)
placelist.sort()
print(placelist)




