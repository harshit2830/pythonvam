#while loop is used to perform iteration
# until the condition is false

#print the no from 1 to 10.

# x=1
# while x<11:
#     print(x)
#     x=x+1 

# #WAP to print the number from 10 to 1

# x=10
# while  x>0:
#     print(x)
#     x=x-1

# #WAP to print table no
# no=int(input("Enter the number for table "))
# a=1
# while a < 11:
#    print(a * no)
#    a=a+1   

# # print table no
# no2=int(input("Enter the number for table "))
# b=10
# while b > 0:
#    print (b * no)
#    b = b - 1   

#WAp to print the pattern using while loop
# 1 4 7 10 14 16
#c=1, operation c=c+3, end point 17
# c=1
# while  c<17:  
#     print(c)
#     c=c+3

#WAP to print the pattern 21 16 11 6 1
# logic c=21 operation c=c-5 endpoint 1
# c=21
# while c>0:
#    print(c)
#    c=c-5
 
#WAP to print the pattern 1 7 19 25     
#logic e=1 endpoint 26 and operation e = e + 6
# e=1
# while e < 26:
#   if e != 13:
#     print(e)
#     e = e + 6 

#function can perform any task
#it can be reuse, function will return the result


#create function to print the name
def printName():
  print("My name is Harshit Dhingra ")
#call function to print the name
  printName()
  #create function to concatenate fname and lname from '
fname=input("Enter your first name ")
lname=input("Enter your last name ")
def printFullName(firstname,lastname):
    print(firstname + " " + lastname)
printFullName(fname ,lname)          
