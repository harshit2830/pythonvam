# -> # is used to comment the line
#-> is also used to define the code meaning
#-> it can also comment and uncomment multiple lines using ctrl+/

#comments example
# write a program to print your name
print("my name is harshit Dhingra") #print function to display statement

#variables can store the values and it can change at any time
name="Harshit Dhingra"

#Pass the variable in the print function
print("My name is "+ name)# + is used to concatenate the strings

#declare and initialize the multiple variables
age=19
gender="male"
email="harshitdhingra555@gmail.com"

#pass the multiple variable in print function
#reason for error str cant't be concatenate with integer

# Problem   
#print("My name is " + name +
#      " my age is " + age + "and gender is " + gender+ email)

#Solution 1: int variables + replace by ,
print("My name is "+name +
      "my age is",age,"and gender is "+ gender)

#solution 2: enclosed the variable inside string statement using f
# Pass the variables in curly braces=P{}
print(f"My name is {name} my age is {age} my gender is {gender} my email is {email}")

#Solution 3: using typecasting 
ageInstring =str(age)
print("My name is " + name +
         " my age is " + ageInstring + "and gender is " + gender+ email)


#Data types in python
print(type(name)) # type function return datatype of variable
print(type(age))
#1. str -> it can store the string data e.g " Harshit Dhingra"
#2. int -> it can store the numeric data e.g age =19
#3. float -> it can store the decimal number e.g percentage =77.8

#Typecasting in python :- conver one datatype to another datatypes
#e.g. Sometime when we purchase item in float we paid in integer
purchaseItemPrice =90.99
paidItemPrice =int(purchaseItemPrice)
print("Paid amount is",paidItemPrice)

#Note -> string can't be converted into int reason string not ascii        

#To get the input from user using input(function
#collegeName= input("Enter your college name ")
#collegeFee  = int(input("Enter your college fee "))
#print("My college name is"+ collegeName, collegeFee)
#Note: - the input function has default return type str

#collegeFee = collegeFee - 25000
#print("After scholorship my fee",collegeFee)

#Find the age in year when bornyear and current year given by user
bornYearAge = int(input("Enter your bornYear age "))
currentAge = int(input("Enter your currentAge year "))
presentAge=currentAge-bornYearAge
print("My current age is ",presentAge)


