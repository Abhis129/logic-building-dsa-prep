'''
PHASE 3 — RECURSION (THINKING IN SELF-REFERENCE)

Goal: Develop logical decomposition and base-condition thinking.
Topics covered: recursive definition, base cases, call stack tracing.
Target Questions: 30–40

Level 1: Foundation of Recursion (Base + Recursive Case)
'''

# 1. Print numbers from 1 to n using recursion
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n)


# 2. Print numbers from n down to 1 using recursion
def print_n_to_1(n):
    if n == 0:
        return
    print(n)
    print_n_to_1(n - 1)


# 3. Print only even numbers from 1 to n recursively
def print_even(n):
    if n == 0:
        return
    print_even(n - 1)
    if n % 2 == 0:
        print(n)


# 4. Print only odd numbers from 1 to n recursively
def print_odd(n):
    if n == 0:
        return
    print_odd(n - 1)
    if n % 2 != 0:
        print(n)


# 5. Print sum of first n natural numbers recursively
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)


# 6. Print factorial of a number recursively
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# 7. Calculate power of a number (x^n) using recursion
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)


# 8. Find nth Fibonacci number recursively
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# 9. Print Fibonacci series up to n terms recursively
def print_fibonacci_series(n):
    for i in range(n):
        print(fibonacci(i), end=" ")
    print()


# 10. Find sum of digits of a number recursively
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

if __name__ == "__main__":
    print_1_to_n(5)
    print_n_to_1(5)
    print_even(10)
    print_odd(10)
    print(sum_n(5))
    print(factorial(5))
    print(power(2, 5))
    print(fibonacci(6))
    print_fibonacci_series(7)
    print(sum_of_digits(1234))