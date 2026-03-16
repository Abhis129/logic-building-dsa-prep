"""
Phase 1 - Conditional Thinking
Level 3 Problems
"""

# Level 3: Math and Number Logic

# 1. Take a 3-digit number and check if all digits are distinct.

num = int(input("Enter a 3-digit number: "))

a = num % 10
b = (num // 10) % 10
c = num // 100

if a != b and a != c and b != c:
    print("All digits are distinct")
else:
    print("Digits are not distinct")


# 2. Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither.

num = int(input("Enter a 3-digit number: "))

first = num // 100
middle = (num // 10) % 10
last = num % 10

if middle > first and middle > last:
    print("Middle digit is the largest")
elif middle < first and middle < last:
    print("Middle digit is the smallest")
else:
    print("Middle digit is neither largest nor smallest")


# 3. Take a 4-digit number and check if the first and last digits are equal.

num = int(input("\nEnter a 4-digit number: "))

first = num // 1000
last = num % 10

if first == last:
    print("First and last digits are equal")
else:
    print("First and last digits are not equal")


# 4. Check whether a given integer is single-digit, double-digit, or multi-digit.

num = int(input("\nEnter a number: "))

digits = len(str(abs(num)))

if digits == 1:
    print("Single digit number")
elif digits == 2:
    print("Double digit number")
else:
    print("Multi digit number")


# 5. Check if a number is a multiple of 7 or ends with 7.

num = int(input("\nEnter a number: "))

if num % 7 == 0 or num % 10 == 7:
    print("Number is multiple of 7 or ends with 7")
else:
    print("Number does not satisfy the condition")


# 6. Take coordinates (x, y) and determine which quadrant the point lies in.

x = int(input("\nEnter x coordinate: "))
y = int(input("Enter y coordinate: "))

if x > 0 and y > 0:
    print("1st Quadrant")
elif x < 0 and y > 0:
    print("2nd Quadrant")
elif x < 0 and y < 0:
    print("3rd Quadrant")
elif x > 0 and y < 0:
    print("4th Quadrant")
else:
    print("Point lies on axis")


# 7. Check if an amount can be evenly divided into 2000, 500, and 100 notes.

amount = int(input("\nEnter amount: "))

if amount % 100 == 0:
    print("Amount can be divided into 2000, 500, and 100 notes")
else:
    print("Amount cannot be divided evenly")


# 8. Check if a number lies within the range [100, 999].

num = int(input("\nEnter a number: "))

if 100 <= num <= 999:
    print("Number is within the range [100, 999]")
else:
    print("Number is outside the range")


# 9. Take two angles of a triangle and compute the third angle.

a = int(input("\nEnter first angle: "))
b = int(input("Enter second angle: "))

c = 180 - (a + b)

print("Third angle is:", c)


# 10. Check whether a number is a perfect square (without using square root).

num = int(input("\nEnter a number: "))

i = 1
while i * i <= num:
    if i * i == num:
        print("Perfect square")
        break
    i += 1
else:
    print("Not a perfect square")