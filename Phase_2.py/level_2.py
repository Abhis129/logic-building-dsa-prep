'''
Phase 2 - Looping & Patterns (Iteration & Flow)
Level 2 - Number-based Looping Logic
'''

# 1. Count the number of digits in a given number
def count_digits(num):
    count = 0
    num = abs(num)
    if num == 0:
        print("Digits:", 1)
        return
    while num > 0:
        count += 1
        num //= 10
    print("Digits:", count)


# 2. Print the reverse of a given number
def reverse_number(num):
    rev = 0
    sign = -1 if num < 0 else 1
    num = abs(num)

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10

    print("Reverse:", sign * rev)


# 3. Check if a number is a palindrome
def is_palindrome(num):
    rev = 0
    temp = abs(num)

    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10

    if num == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")


# 4. Find the sum of digits of a number
def sum_of_digits(num):
    total = 0
    num = abs(num)

    while num > 0:
        total += num % 10
        num //= 10

    print("Sum of digits:", total)


# 5. Check if a number is an Armstrong number
def is_armstrong(num):
    temp = num
    count = 0

    # count digits
    while temp > 0:
        count += 1
        temp //= 10

    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** count
        temp //= 10

    if total == num:
        print("Armstrong Number")
    else:
        print("Not Armstrong")


# 6. Check if a number is a perfect number
def is_perfect(num):
    if num <= 1:
        print("Not Perfect Number")
        return

    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div += i

    if sum_div == num:
        print("Perfect Number")
    else:
        print("Not Perfect Number")


# 7. Print all prime numbers between 1 and 100
def print_primes_1_to_100():
    print("Prime numbers from 1 to 100:")
    for num in range(2, 101):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
    print()


# 8. Check if a number is prime or not
def is_prime(num):
    if num <= 1:
        print("Not Prime")
        return

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            return

    print("Prime")


# 9. Print Fibonacci series up to n terms
def fibonacci_series(n):
    a, b = 0, 1
    print("Fibonacci series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


# 10. Print sum of first n terms of Fibonacci series
def fibonacci_sum(n):
    a, b = 0, 1
    total = 0

    for _ in range(n):
        total += a
        a, b = b, a + b

    print("Fibonacci Sum:", total)