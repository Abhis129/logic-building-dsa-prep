"""
Phase 2 - Looping & Patterns (Iteration & Flow)
Level 3: Mathematical & Logical Patterns
"""

# 1. Print squares of numbers from 1 to n
n = int(input("Enter n: "))
for i in range(1, n+1):
    print(i*i)


# 2. Print cubes of numbers from 1 to n
n = int(input("Enter n: "))
for i in range(1, n+1):
    print(i**3)


# 3. Print all numbers between a and b divisible by 7
a = int(input("Enter a: "))
b = int(input("Enter b: "))
for i in range(a, b+1):
    if i % 7 == 0:
        print(i)


# 4. Find HCF (GCD) of two numbers using loops
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
hcf = 1
for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        hcf = i
print("HCF =", hcf)


# 5. Find LCM of two numbers using loops
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
max_num = max(a, b)
while True:
    if max_num % a == 0 and max_num % b == 0:
        print("LCM =", max_num)
        break
    max_num += 1


# 6. Print all factors of a given number
n = int(input("Enter number: "))
for i in range(1, n+1):
    if n % i == 0:
        print(i)


# 7. Find the sum of all factors of a number
n = int(input("Enter number: "))
sum_factors = 0
for i in range(1, n+1):
    if n % i == 0:
        sum_factors += i
print("Sum =", sum_factors)


# 8. Check if a number is a strong number
n = int(input("Enter number: "))
temp = n
sum_fact = 0

while temp > 0:
    digit = temp % 10
    
    fact = 1
    for i in range(1, digit+1):
        fact *= i
    
    sum_fact += fact
    temp //= 10

if sum_fact == n:
    print("Strong number")
else:
    print("Not a strong number")


# 9. Print first n terms of an arithmetic progression (a, d)
a = int(input("Enter first term: "))
d = int(input("Enter common difference: "))
n = int(input("Enter n: "))

for i in range(n):
    print(a + i*d)


# 10. Print first n terms of a geometric progression (a, r)
a = int(input("Enter first term: "))
r = int(input("Enter common ratio: "))
n = int(input("Enter n: "))

term = a
for i in range(n):
    print(term)
    term *= r