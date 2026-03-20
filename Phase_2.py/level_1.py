"""
Phase 2 - Looping & Patterns (Iteration & Flow)
Level 1: Basic Looping (Introductory)
"""

# Levle 1 Problems

# 1. Print numbers from 1 to 10
print("1. Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)


# 2. Print all even numbers between 1 and 100
print("\n2. Even numbers from 1 to 100:")
for i in range(1, 101):
    if i % 2 == 0:
        print(i)


# 3. Print all odd numbers between 1 and 100
print("\n3. Odd numbers from 1 to 100:")
for i in range(1, 101):
    if i % 2 != 0:
        print(i)


# 4. Print numbers from 10 down to 1
print("\n4. Numbers from 10 to 1:")
for i in range(10, 0, -1):
    print(i)


# 5. Print the table of a given number
print("\n5. Table of a number:")
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# 6. Print the sum of first n natural numbers
print("\n6. Sum of first n natural numbers:")
n = int(input("Enter n: "))
sum_n = 0
for i in range(1, n + 1):
    sum_n += i
print("Sum =", sum_n)


# 7. Print the sum of all even numbers up to n
print("\n7. Sum of even numbers up to n:")
n = int(input("Enter n: "))
even_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
print("Even Sum =", even_sum)


# 8. Print the sum of all odd numbers up to n
print("\n8. Sum of odd numbers up to n:")
n = int(input("Enter n: "))
odd_sum = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        odd_sum += i
print("Odd Sum =", odd_sum)


# 9. Print the factorial of a given number
print("\n9. Factorial of a number:")
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial =", fact)


# 10. Print the product of digits of a given number
print("\n10. Product of digits:")
num = int(input("Enter a number: "))
product = 1

while num > 0:
    digit = num % 10
    product *= digit
    num //= 10

print("Product of digits =", product)
