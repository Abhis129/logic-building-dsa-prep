'''
PHASE 3 — RECURSION (THINKING IN SELF-REFERENCE)
Level-2 Number-based Recursive Thinking
'''

# 1. Count the number of digits in a number recursively
def count_digits(n):
    if n == 0:
        return 1
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


# 2. Reverse a number recursively
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)


# 3. Check if a number is a palindrome using recursion
def is_palindrome(n):
    return n == reverse_number(n)


# 4. Find product of digits of a number recursively
def product_of_digits(n):
    if n == 0:
        return 1
    return (n % 10) * product_of_digits(n // 10)


# 5. Find GCD (HCF) of two numbers using Euclid’s algorithm recursively
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# 6. Convert a number to binary recursively
def to_binary(n):
    if n == 0:
        return ""
    return to_binary(n // 2) + str(n % 2)


# 7. Print digits of a number in words recursively
def number_to_words(n):
    words = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    if n < 10:
        return words[n]
    return number_to_words(n // 10) + " " + words[n % 10]


# 8. Calculate the sum of first n even numbers recursively
def sum_even(n):
    if n == 0:
        return 0
    return 2 * n + sum_even(n - 1)


# 9. Calculate the sum of first n odd numbers recursively
def sum_odd(n):
    if n == 0:
        return 0
    return (2 * n - 1) + sum_odd(n - 1)


# 10. Find nCr (Combination) recursively using Pascal’s relation
def nCr(n, r):
    if r == 0 or r == n:
        return 1
    return nCr(n - 1, r - 1) + nCr(n - 1, r)


if __name__ == "__main__":
    print(count_digits(12345))
    print(reverse_number(1234))
    print(is_palindrome(121))
    print(product_of_digits(1234))
    print(gcd(48, 18))
    print(to_binary(10))
    print(number_to_words(123))
    print(sum_even(5))
    print(sum_odd(5))
    print(nCr(5, 2))