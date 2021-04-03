# Day 8-1 
import math
def paint_calc(height, width, cover):
  cnt = int(math.ceil(height * width / cover))
  print(f"You'll need {cnt} cans of paint.")

# Day 8-2
import math

def prime_checker(number):
  stop = int(math.sqrt(number))
  
  for i in range(2, stop+1):
    if number % i == 0:
      print("It's not a prime number.")
      return
  
  print("It's a prime number.")

# Project caesar-cipher-1

def encrypt(text, shift):
  cipher_text = ""
  for i in range(len(text)):
    if text[i] in alphabet:
      j = (alphabet.index(text[i]) + shift) % len(alphabet)
      cipher_text += alphabet[j]
    else:
      cipher_text += text[i]
  print(f"The encoded text is {cipher_text}")

encrypt(text, shift)

# Project caesar-cipher-2

def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")

if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  decrypt(cipher_text=text, shift_amount=shift)
else :
  print("error calling")

# Project caesar-cipher-3
def caesar(message, shift, direction):
  tp = "encoded"
  sft = shift
  if direction == "decode":
    tp = "decoded"
    sft = -shift
  
  text = ""
  for letter in message:
    position = alphabet.index(letter)
    new_position = position + sft
    text += alphabet[new_position]
  print(f"The {tp} text is {text}")

caesar(message=text, shift=shift, direction=direction)

# Project caesar-cipher-4

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  shift_amount %= len(alphabet)
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:    
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")


import art
print(art.logo)

ans = "yes"
while ans == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  ans = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()