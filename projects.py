#create first python project to generate 6 digit random otp

import random

def generate_otp():
    otp = random.randint(100000, 999999)
    return otp

print("Your 6-digit OTP is:", generate_otp())

#WAP to convert dollar into rupees and vice versa

def convert_currency():
    # Exchange rate (1 USD = 74.83 INR, you can update this value as per current exchange rate)
    exchange_rate = 74.83

    print("1. Convert Dollars to Rupees")
    print("2. Convert Rupees to Dollars")
    choice = int(input("Enter your choice (1/2): "))

    if choice == 1:
        dollars = float(input("Enter amount in Dollars: "))
        rupees = dollars * exchange_rate
        print(f"{dollars} USD is equal to {rupees} INR")
    elif choice == 2:
        rupees = float(input("Enter amount in Rupees: "))
        dollars = rupees / exchange_rate
        print(f"{rupees} INR is equal to {dollars} USD")
    else:
        print("Invalid choice")

convert_currency()


#WAP to find the age when the birth year is given

import datetime

def calculate_age():
    birth_year = int(input("Enter your birth year: "))
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    print(f"Your age is: {age} years")

calculate_age()