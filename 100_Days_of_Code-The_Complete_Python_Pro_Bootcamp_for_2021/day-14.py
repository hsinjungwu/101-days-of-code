import art
import random
from game_data import data
from replit import clear

def get_bID(aID):
  shift = random.randint(1, len(data)-1)
  return (aID+shift) % len(data)
  
def data_info(sd):
  name = sd["name"]
  description = sd["description"]
  country = sd["country"]  
  return f"{name}, {description}, from {country}."

def check_guess(da, db, guessA):
  daf = da["follower_count"]
  dbf = db["follower_count"]
  if daf > dbf:
    return guessA  
  else:
    return not guessA

def game():
  aID = random.randint(0, len(data)-1)
  dataA = data[aID]
  score = 0
  
  guessRight = True
  while guessRight:
    print(art.logo)
    if score > 0:
      print(f"You're right! Current score: {score}.")
    print(f"Compare A: {data_info(dataA)}")
    print(art.vs)
    bID = get_bID(aID)
    dataB = data[bID]
    print(f"Against B: {data_info(dataB)}")
    guessA = input("Who has more followers? Type 'A' or 'B': ").upper() == "A"
    guessRight = check_guess(dataA, dataB, guessA)
    if guessRight:
      score += 1
      aID = bID
      dataA = dataB
    clear()
      
  print(art.logo)
  print(f"Sorry, that's wrong. Final score: {score}")
  
game()