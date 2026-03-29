'''
PHASE 4 — BASIC ARRAYS (Iterative Logical Thinking)
Level 2: Searching & Counting Logic
'''

# 1. Input an element x — check if it exists in the array.
def exists(arr, x, i=0):
    if i == len(arr):
        return False
    if arr[i] == x:
        return True
    return exists(arr, x, i + 1)


# 2. Count how many times a given element appears.
def count_occ(arr, x, i=0):
    if i == len(arr):
        return 0
    return (1 if arr[i] == x else 0) + count_occ(arr, x, i + 1)


# 3. Find the first occurrence of a given number.
def first_occ(arr, x, i=0):
    if i == len(arr):
        return -1
    if arr[i] == x:
        return i
    return first_occ(arr, x, i + 1)


# 4. Find the last occurrence of a given number.
def last_occ(arr, x, i=0):
    if i == len(arr):
        return -1
    res = last_occ(arr, x, i + 1)
    if res != -1:
        return res
    if arr[i] == x:
        return i
    return -1


# 5. Check if all elements in an array are unique.
def is_unique(arr, i=0, j=1):
    if i == len(arr):
        return True
    if j == len(arr):
        return is_unique(arr, i + 1, i + 2)
    if arr[i] == arr[j]:
        return False
    return is_unique(arr, i, j + 1)


# 6. Find the sum of even elements only.
def sum_even(arr, i=0):
    if i == len(arr):
        return 0
    return (arr[i] if arr[i] % 2 == 0 else 0) + sum_even(arr, i + 1)


# 7. Find the sum of odd elements only.
def sum_odd(arr, i=0):
    if i == len(arr):
        return 0
    return (arr[i] if arr[i] % 2 != 0 else 0) + sum_odd(arr, i + 1)


# 8. Find the count of prime numbers in the array.
def is_prime(n, d=2):
    if n < 2:
        return False
    if d * d > n:
        return True
    if n % d == 0:
        return False
    return is_prime(n, d + 1)

def count_primes(arr, i=0):
    if i == len(arr):
        return 0
    return (1 if is_prime(arr[i]) else 0) + count_primes(arr, i + 1)


# 9. Count how many numbers are divisible by 3 and 5 both.
def count_div_3_5(arr, i=0):
    if i == len(arr):
        return 0
    return (1 if arr[i] % 15 == 0 else 0) + count_div_3_5(arr, i + 1)


# 10. Count how many elements are perfect squares.
def is_perfect_square(n, i=1):
    if i * i > n:
        return False
    if i * i == n:
        return True
    return is_perfect_square(n, i + 1)

def count_perfect_squares(arr, i=0):
    if i == len(arr):
        return 0
    return (1 if is_perfect_square(arr[i]) else 0) + count_perfect_squares(arr, i + 1)


# Demo
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 9, 15, 16, 2]

    print("1:", exists(arr, 3))
    print("2:", count_occ(arr, 2))
    print("3:", first_occ(arr, 2))
    print("4:", last_occ(arr, 2))
    print("5:", is_unique(arr))
    print("6:", sum_even(arr))
    print("7:", sum_odd(arr))
    print("8:", count_primes(arr))
    print("9:", count_div_3_5(arr))
    print("10:", count_perfect_squares(arr))