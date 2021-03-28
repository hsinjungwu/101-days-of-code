# Day 3-1 Exercise
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

# Day 3-2 Exercise
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight / height ** 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

# Day 3-3 Exercise
year = int(input("Which year do you want to check? "))
if year % 400 == 0:
  print("Leap year.")
elif year % 100 == 0:
  print("Not leap year.")
elif year % 4 == 0:
  print("Leap year.")
else:    
  print("Not leap year.")

# Day 3-4 Exercise
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
  bill = 15
elif size == "M":
  bill = 20
else:
  bill = 25
  
if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")

# Day 3-5 Exercise
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

un = (name1+name2).upper()

score_true = 0
score_true += un.count("T")
score_true += un.count("R")
score_true += un.count("U")
score_true += un.count("E")

score_love = 0
score_love += un.count("L")
score_love += un.count("O")
score_love += un.count("V")
score_love += un.count("E")

score = int(str(score_true) + str(score_love))

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else: 
  print(f"Your score is {score}.")

# Project Treaure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

lr = input("Left or Right? ").upper()
if lr == "RIGHT":
  sw = input("Swim or Wait? ").upper()
  if sw == "WAIT":
    br = input("Blue, Yellow or Red? ").upper()
    if br == "YELLOW":
      print("You WIN!!")
    else:
      print(f"Wrong Color {br}. GAME OVER!!")
  else:
    print(f"Wrong Action {sw}. GAME OVER!!")    
else:
  print(f"Wrong Direction {lr}. GAME OVER!!")