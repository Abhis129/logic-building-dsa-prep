"""
Phase 2 - Looping & Patterns (Iteration & Flow)
Level 5: Logical Loop Combinations
"""

# 1. Print all numbers whose sum of digits is even (1–100)
for i in range(1, 101):
    temp = i
    s = 0
    while temp > 0:
        s += temp % 10
        temp //= 10
    if s % 2 == 0:
        print(i)


# 2. Count numbers between 1–500 divisible by 7 but not by 5
count = 0
for i in range(1, 501):
    if i % 7 == 0 and i % 5 != 0:
        count += 1
print("Count =", count)


# 3. Print palindrome numbers between 1–500
for i in range(1, 501):
    num = i
    rev = 0
    temp = num
    while temp > 0:
        rev = rev * 10 + (temp % 10)
        temp //= 10
    if num == rev:
        print(num)


# 4. Print numbers between 1–100 whose digit sum is multiple of 3
for i in range(1, 101):
    temp = i
    s = 0
    while temp > 0:
        s += temp % 10
        temp //= 10
    if s % 3 == 0:
        print(i)


# 5. Find smallest and largest digit in a number
n = int(input("Enter number: "))
small = 9
large = 0

while n > 0:
    digit = n % 10
    if digit < small:
        small = digit
    if digit > large:
        large = digit
    n //= 10

print("Smallest digit =", small)
print("Largest digit =", large)


# 6. Print numbers from 1–n with even number of 1s in binary
n = int(input("Enter n: "))
for i in range(1, n+1):
    binary = bin(i)[2:]
    count = 0
    for ch in binary:
        if ch == '1':
            count += 1
    if count % 2 == 0:
        print(i)


# 7. Pattern where each row i prints i*i
n = int(input("Enter n: "))
for i in range(1, n+1):
    for j in range(i):
        print(i*i, end=" ")
    print()


# 8. Print factorial of each number from 1 to n
n = int(input("Enter n: "))
for i in range(1, n+1):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    print("Factorial of", i, "=", fact)


# 9. Sum of odd and even digits separately
n = int(input("Enter number: "))
odd_sum = 0
even_sum = 0

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit
    n //= 10

print("Sum of even digits =", even_sum)
print("Sum of odd digits =", odd_sum)


# 10. Take 5 numbers, skip 0 using continue, sum others
total = 0
for i in range(5):
    num = int(input("Enter number: "))
    if num == 0:
        continue
    total += num

print("Sum =", total)