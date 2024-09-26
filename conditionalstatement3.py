#condiyional statement will check the condition is true or not
#to check the condition we use if else

#WAP to the user eligible for voting
userAge= int(input("Enter your age"))
#Note the default input function return type is string 
#For vote user age must be freater than 18
if userAge >18:
       print("You are eligible for voting ")
else:
       print("you are not eligible for voting ")

#WAP to check the user can sit in the first compartment for metro.
userGender = input("Enter your gender")
#To check the user is male or female
if  userGender == "male":    
    print("You are not eligible for sitting in first metro compartment")
elif userGender  == "female":
      print("You are eligible for sitting in first metro compartment")

else:
    print("You can sit in any compartment")

#WAP if gender is female and age greater than 18-> govt job apply
#else male age greater than ->18 private job apply

userGender = input("Enter your gender ")
userAge = int(input("Enter your age "))

if userGender  == "female" and userAge > 18:
      print("you are eligible for apply in government job")
elif  userGender == "male" and userAge > 18:
      print("you are eligible for apply in private job")      
else:
      print("you are under age")

