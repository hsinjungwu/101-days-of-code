# Day 4-1 Exercise
import random

r = random.randint(0, 1)
if r == 1:
  print("Heads")
else:
  print("Tails")

# Day 4-2 Exercise
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

idx = random.randint(0, len(names)-1)
name = names[idx]
print(f"{name} is going to buy the meal today!")

# Project Rock Paper Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

c = [rock, paper, scissors]
h = int(input("What do you choose ? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
if h < 0 or h >= len(c):
  print(f"Invalid Number {h} !!")
else:
  print(c[h])
  print("Computer Choice:")
  p = random.randint(0, 2)
  print(c[p])

  if h == p:
    print("Tie")
  elif (h+1)%3 == p:
    print("You Lose!!")
  else:
    print("You Win!!")