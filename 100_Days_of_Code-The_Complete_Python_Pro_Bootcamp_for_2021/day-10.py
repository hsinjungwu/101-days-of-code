# Day 10-1 
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  days = month_days[month-1]
  if month == 2 and is_leap(year):
    return days+1
  else:
    return days
  
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# Day 10-2
import art
print(art.logo)

def add(n1, n2):
  return n1+n2

def sub(n1, n2):
  return n1-n2

def mul(n1, n2):
  return n1*n2

def div(n1, n2):
  return n1/n2

ops = {
  "+": add,
  "-": sub,
  "*": mul,
  "/": div,
}

def firstNumber(prevN, usePrevN):
  if usePrevN:
    return prevN
  else:
    return float(input("What's the first number? "))


keep = True
usePrevN = False
nv = 0
while keep:
  n1 = firstNumber(nv, usePrevN)
  for o in ops:
    print(o)
  op = input("pick an operation: ")
  n2 = float(input("What's the next number? "))
  nv = ops[op](n1,n2)
  print(f"{n1} {op} {n2} = {nv}")
  tp = input(f"Type 'y' to continue calc with {nv} or type 'n' to start a new calc. ").lower()
  if tp == "y":
    usePrevN = True
  elif tp == "n":
    usePrevN = False
  else:
    keep = False