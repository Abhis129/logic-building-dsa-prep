"""
Phase 1 - Conditional Thinking
Level 2 Problems
"""

# Level 2: Nested If & Multiple Conditions


# 1. Take three sides and check if they form a valid triangle.
side1 = int(input("Enter 1st side: "))
side2 = int(input("Enter 2nd side: "))
side3 = int(input("Enter 3rd side: "))

if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
    print("Valid Triangle")
else:
    print("Not a Valid Triangle")


# 2. If the sides form a valid triangle, determine whether it is equilateral, isosceles, or
# scalene.

side1 = int(input("Enter 1st side: "))
side2 = int(input("Enter 2nd side: "))
side3 = int(input("Enter 3rd side: "))

if side1 == side2 == side3:
    print("This is an Equilateral Triangle.")

elif side1 == side2 or side2 == side3 or side1 == side3:
    print("This is a Isosceles Triangle.")

else:
    print("This is an Scalene Triangle.")

# 3. Take marks (0–100) and print the corresponding grade (A/B/C/D/F).

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif 70 <= marks <= 89:
    print("Grade B")
elif 50 <= marks <= 69:
    print("Grade C")
elif 40 <= marks <= 49:
    print("Grade D")
else:
    print("Grade F")


# 4. Check if one of two given numbers is a multiple of the other.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % num2 == 0 or num2 % num1 == 0:
    print("One number is a multiple of the other")
else:
    print("They are not multiples of each other")

# 5. Take the hour of the day (0–23) and print “Good Morning”, “Good Afternoon”, “Good
# Evening”, or “Good Night”.
hour = int(input("Enter hour (0-23): "))

if 5 <= hour <= 11:
    print("Good Morning")
elif 12 <= hour <= 16:
    print("Good Afternoon")
elif 17 <= hour <= 20:
    print("Good Evening")
else:
    print("Good Night")

# 6. Check voting eligibility for a given age (18+).
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# 7. Take two numbers and determine whether both are even, both are odd, or one is
# even and one is odd.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both numbers are odd")
elif num1 % 2 == 0:
    print(num1, "is an even number", num2, "is an odd number")
else:
    print(num2, "is an even number", num1, "is an odd number")

# 8. Take an alphabet character and check if it lies between ‘a’ and ‘m’ or ‘n’ and ‘z’.
letter = input("Enter an alphabet: ").lower()

if 'a' <= letter <= 'm':
    print("The letter is between a and m")
elif 'n' <= letter <= 'z':
    print("The letter is between n and z")
else:
    print("Invalid input")

# 9. Take a day number (1–7) and print the corresponding day name.
day = int(input("Enter day number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day number")

# 10. Take a month  number (1–12) and print the number of days in that month (ignore leap
# years).
month = int(input("Enter month number (1-12): "))

if month == 2:
    print("28 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
elif month in [1,3,5,7,8,10,12]:
    print("31 days")
else:
    print("Invalid month number")