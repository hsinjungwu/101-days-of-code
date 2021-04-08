#Number Guessing Game Objectives:

from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

ans = random.randint(1, 100)

attempts = 5
if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == "easy":
  attempts = 10

while attempts > 0:
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if guess == ans:
    print(f"You got it! The answer was {ans}.")
    break
  else:
    attempts -= 1
    if guess < ans:
      print("Too low")
    else:
      print("Too high")
    
    if attempts == 0:
      print(f"Answer = {ans}. You've run out of guesses, you lose.")
    else:
      print("Guess again.")