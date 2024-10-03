# File handling:- Work on the file

# Create File:- syntax
# variableName = open("filename.extension", "filemode")
# e.g 
# myLaptopPassword = open("password.txt", "w")

# Write file:- syntax
# e.g. myLaptopPassword.write("guhiguhi")

# Read from file
# e.g myLaptopPassword.read()

# Delete file
# import os
# os.remove("password.txt")

#create file for saving my laptop password
#open function will create then file
#when file is not exist and write the file
myPassword = open("password.txt", "w")


#write my laptop password in fil
myPassword.write("my asus password is -harshit2812")

#overwrite the new password
# myPassword.write(input("Enter the new password: "))


#read the password from file
myPassword = open("password.txt","r")
mydata = myPassword.read()
if "asus" in mydata:
   print("yes")
else:
   print("no")   

#close the file
myPassword.close()

#delete the file
import os
os.remove("password.txt")

#create read write delete csv, excel, json, txt
# #create csv file 
# myCsv =  open("myfile", "w")
# myCsv.write("pawan,tripti,amjali,saloni,suryansh")

# myexcel = open("myexcel.xlsx","w")
# myexcel.write("pawan,tripti,amjali,saloni,suryansh"s)

