# Day 5-1 Exercise
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

height_sum = 0
count = 0

for h in student_heights:
  height_sum += h
  count+=1

avg = round(height_sum/count)
print(avg)

# Day 5-2 Exercise
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

h = student_scores[0]
for s in student_scores:
  if s > h:
    h = s

# Day 5-3 Exercise
total = 0
for i in range(2, 101, 2):
  total += i

print(total)

print(f"The highest score in the class is: {h}")

# Day 5-4 Exercise
for i in range(1,101):
  if i%15 == 0:
    print("FizzBuzz")
  elif i%3 == 0:
    print("Fizz")    
  elif i%5 == 0:
    print("Buzz")
  else:
    print(i)

# Project Password Generator 
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
chls = []
pswd = ""
for i in range(0, nr_letters):
  l = random.choice(letters)
  pswd += l
  chls.append(l)

for i in range(0, nr_symbols):
  s = random.choice(symbols)
  pswd += s
  chls.append(s)

for i in range(0, nr_numbers):
  n = random.choice(numbers)
  pswd += n
  chls.append(n)

print(pswd)
#Hard Level - Order of characters randomised:

random.shuffle(chls)
npswd = ""
for c in chls:
  npswd += c
print(npswd)