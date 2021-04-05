# Day 9-1 
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}

for student in student_scores:
  score = student_scores[student]
  if score <= 70:
    student_grades[student] = "Fail"
  elif score <= 80:
    student_grades[student] = "Acceptable"
  elif score <= 90:
    student_grades[student] = "Exceeds Expectations"
  else:
    student_grades[student] = "Outstanding"
print(student_grades)

# Day 9-2
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(country, visits, cities):
  travel_log.append({    
    "country": country,
    "visits": visits,
    "cities": cities
  })

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# Day 9-3
from replit import clear
import art
print(art.logo)
bid_data = {}

end = False
while not end:
  name = input("What is your name? ")
  bid = int(input("What is your bid? "))
  bid_data[name] = bid
  ans = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  if ans == "yes":
    clear()
  elif ans == "no":
    end = True


max_bid = 0
max_bidder = ""
for name in bid_data:
  bid = bid_data[name]
  if bid >= max_bid:
    max_bidder = name
    max_bid = bid

print(f"The winner is {max_bidder} with bid {max_bid}")