# Day 2-1 Exercise
two_digit_number = input("Type a two digit number: ")
n = int(two_digit_number)
a = n//10
b = n%10
print(a+b)

# Day 2-2 Exercise
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
h = float(height)
w = float(weight)
bmi = int(w / h ** 2)
print(str(bmi))

# Day 2-3 Exercise
age = input("What is your current age?")
a = 90-int(age)
x = 365*a
y = 52*a
z = 12*a
print(f"You have {x} days, {y} weeks, and {z} months left.")

# Project : Tip Calculator
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip_p = float(input("What percentage tip would you like to give? 10, 12 or 15? "))/100
people = float(input("How many people split the bill? "))
pay = round(bill * (1+tip_p) / people, 2)
f_pay = "{0:.2f}".format(pay)
print(f"Each person should pay : ${f_pay}")