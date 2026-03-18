"""
Phase 2 – Looping & Patterns (Iteration & Flow)
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

