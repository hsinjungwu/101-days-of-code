############### Blackjack Project #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
from art import logo

def deal():
  deal_cards = []
  for i in range(2):
    deal_cards.append(random.choice(cards))
  return deal_cards

def score(dcards):
  s = sum(dcards)
  i = 0
  while s > 21 and 11 in dcards:    
    if dcards[i] == 11:
      dcards[i] -= 10
      s -= 10
    i += 1
  return s

def compare(pScore, dScore):
  if pScore > 21:
    print("You Lose")
  elif dScore > 21:
    print("You Win!!")
  elif dScore > pScore:
    print("You Lose")
  elif dScore < pScore:
    print("You Win!!")
  else:
    print("TIE!!")


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ") == "y"
if play:
  print(logo)
  
  playerCards = deal()  
  playerScore = score(playerCards)
            
  dealerCards = deal()
  while playerScore <= 21:
    print(f"Your cards: {playerCards}, current score: {playerScore}");
    print(f"Computer's first card: {dealerCards[0]}"); 
  
    act = input("Type 'y' to get another card, type 'n' to pass: ")
    if act == "y":
      playerCards.append(random.choice(cards))
      playerScore = score(playerCards)      
    elif act == "n":
      break

print(f"Your final hand: {playerCards}, final score: {playerScore}")
dealerScore = score(dealerCards)
if playerScore <= 21 and dealerScore < 17:
  dealerCards.append(random.choice(cards))
  dealerScore = score(dealerCards)

print(f"Computer's final hand: {dealerCards}, final score: {dealerScore}")
compare(playerScore, dealerScore)  