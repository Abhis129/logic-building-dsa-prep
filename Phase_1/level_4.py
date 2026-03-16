"""
Phase 1 - Conditional Thinking
Level 4 Problems
"""


# Level 4: Logical Operators & Compound Statements


# 1. Take a character and check if it is a letter, a digit, or neither.

ch = input("Enter a character: ")

if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
    print("It is a letter")
elif '0' <= ch <= '9':
    print("It is a digit")
else:
    print("Neither letter nor digit")


# 2. Take a number and print “Fizz” if divisible by 3, “Buzz” if divisible by 5,
# and “FizzBuzz” if divisible by both.

num = int(input("\nEnter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print("None")


# 3. Take three numbers and print the median value (neither maximum nor minimum).

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a >= b and a <= c) or (a <= b and a >= c):
    print("Median:", a)
elif (b >= a and b <= c) or (b <= a and b >= c):
    print("Median:", b)
else:
    print("Median:", c)


# 4. Take 24-hour time (hours and minutes) and print whether it is AM or PM.

hour = int(input("\nEnter hour (0-23): "))
minute = int(input("Enter minutes (0-59): "))

if 0 <= hour < 12:
    print("AM")
elif 12 <= hour <= 23:
    print("PM")
else:
    print("Invalid time")


# 5. Take income and age, and check if eligible for tax.

income = int(input("\nEnter income: "))
age = int(input("Enter age: "))

if age > 18 and income > 500000:
    print("Eligible for tax")
else:
    print("Not eligible for tax")


# 6. Take two numbers and check if both are positive and their sum is less than 100.

x = int(input("\nEnter first number: "))
y = int(input("Enter second number: "))

if x > 0 and y > 0 and (x + y) < 100:
    print("Condition satisfied")
else:
    print("Condition not satisfied")


# 7. Take a single digit (0–9) and print its word form.

digit = int(input("\nEnter a digit (0-9): "))

if digit == 0:
    print("Zero")
elif digit == 1:
    print("One")
elif digit == 2:
    print("Two")
elif digit == 3:
    print("Three")
elif digit == 4:
    print("Four")
elif digit == 5:
    print("Five")
elif digit == 6:
    print("Six")
elif digit == 7:
    print("Seven")
elif digit == 8:
    print("Eight")
elif digit == 9:
    print("Nine")
else:
    print("Invalid digit")


# 8. Take a weekday number (1–7) and determine if it is a weekday or weekend.

day = int(input("\nEnter day number (1-7): "))

if 1 <= day <= 5:
    print("Weekday")
elif day == 6 or day == 7:
    print("Weekend")
else:
    print("Invalid input")


# 9. Take electricity units consumed and calculate the bill as per slabs.

units = int(input("\nEnter electricity units: "))

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = (100 * 1.5) + (units - 100) * 2
elif units <= 300:
    bill = (100 * 1.5) + (100 * 2) + (units - 200) * 3
else:
    bill = (100 * 1.5) + (100 * 2) + (100 * 3) + (units - 300) * 5

print("Electricity Bill:", bill)


# 10. Take a password string and check basic rules (length ≥ 8 and contains at least one digit).

password = input("\nEnter password: ")

has_digit = False

for char in password:
    if '0' <= char <= '9':
        has_digit = True

if len(password) >= 8 and has_digit:
    print("Valid password")
else:
    print("Invalid password")