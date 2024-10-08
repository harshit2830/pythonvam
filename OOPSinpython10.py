#OOPS in Python

#Object oriented programming -> objects

#class -> it is a container which collection variables, functions
# Example -> tripti class
# tripti.fullname = "triptisahu"
# tripti.age = 19
# tripti.sleeping()
# tripti.eating()
# tripti.watching()
# class syntax
class ClassName : 
    print("This is my class") 
class Harshit:
    age = 19
    fullName = "Harshit Dhingra"
    email="harshitdhingra222@gmail.com"
    def pocketMoney(this,amount):
        print("My pocket money is", amount) 
    def monthlySalary(this, daySalary):
        totalSalary=31*daySalary
        print("My monthly salary is", totalSalary)

#create class object
harshit:Harshit = Harshit()
harshit.pocketMoney(15000)
harshit.monthlySalary(int(input("Enter your one day salary")))
print(harshit.fullName , harshit.age ,  harshit.email) 


