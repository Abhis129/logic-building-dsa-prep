"""
Phase 1 - Conditional Thinking
Level 5 Creative / Tricky Logical Scenarios Problems
"""


# 1. Check if point lies on X-axis, Y-axis, or Origin

x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

if x == 0 and y == 0:
    print("Point is at the Origin")
elif y == 0:
    print("Point lies on X-axis")
elif x == 0:
    print("Point lies on Y-axis")
else:
    print("Point lies somewhere in the plane")


# 2. Check Pythagorean Triplet

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print("Pythagorean Triplet")
else:
    print("Not a Pythagorean Triplet")


# 3. Check valid calendar date (ignoring leap year)

day = int(input("\nEnter day: "))
month = int(input("Enter month: "))

if month < 1 or month > 12:
    print("Invalid date")

elif month in [1,3,5,7,8,10,12] and 1 <= day <= 31:
    print("Valid date")

elif month in [4,6,9,11] and 1 <= day <= 30:
    print("Valid date")

elif month == 2 and 1 <= day <= 28:
    print("Valid date")

else:
    print("Invalid date")


# 4. Smaller angle between clock hands

hour = int(input("\nEnter hour: "))
minute = int(input("Enter minute: "))

hour_angle = (hour % 12) * 30 + minute * 0.5
minute_angle = minute * 6

angle = abs(hour_angle - minute_angle)
smaller_angle = min(angle, 360 - angle)

print("Smaller angle:", smaller_angle)


# 5. Check Arithmetic Progression

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if b - a == c - b:
    print("Numbers are in Arithmetic Progression")
else:
    print("Not in Arithmetic Progression")


# 6. Check Geometric Progression

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a != 0 and b != 0 and b/a == c/b:
    print("Numbers are in Geometric Progression")
else:
    print("Not in Geometric Progression")


# 7. Check 3-digit rule (first + last = middle)

num = int(input("\nEnter a 3-digit number: "))

first = num // 100
middle = (num // 10) % 10
last = num % 10

if first + last == middle:
    print("Condition satisfied")
else:
    print("Condition not satisfied")


# 8. Sum of digits greater than product

num = int(input("\nEnter a number (1-9999): "))

temp = num
sum_digits = 0
product = 1

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    product *= digit
    temp //= 10

if sum_digits > product:
    print("Sum of digits is greater than product")
else:
    print("Product is greater or equal")


# 9. Compare two dates

day1 = int(input("\nEnter first date day: "))
month1 = int(input("Enter first date month: "))

day2 = int(input("Enter second date day: "))
month2 = int(input("Enter second date month: "))

if month1 < month2 or (month1 == month2 and day1 < day2):
    print("First date comes earlier")
elif month1 == month2 and day1 == day2:
    print("Both dates are same")
else:
    print("Second date comes earlier")


# 10. Find century from year

year = int(input("\nEnter year: "))

century = (year - 1) // 100 + 1

print("Century:", century)