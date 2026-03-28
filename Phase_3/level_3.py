'''
PHASE 3 — RECURSION (THINKING IN SELF-REFERENCE)
Level-3 Pattern and Printing Problems
'''


# 1. Print a line of n stars
def line_stars(n):
    if n == 0:
        return
    print("*", end="")
    line_stars(n - 1)


# 2. Print square of stars (n x n)
def square_stars(n, row=0):
    if row == n:
        return
    line_stars(n)
    print()
    square_stars(n, row + 1)


# 3. Triangle (top-down)

def triangle_top_down(n):
    if n == 0:
        return
    line_stars(n)
    print()
    triangle_top_down(n - 1)


# 4. Triangle (bottom-up)
def triangle_bottom_up(n):
    if n == 0:
        return
    triangle_bottom_up(n - 1)
    line_stars(n)
    print()


# 5. Number pattern (1 to n each row)

def print_numbers(n, i=1):
    if i > n:
        return
    print(i, end=" ")
    print_numbers(n, i + 1)

def number_pattern(n):
    if n == 0:
        return
    number_pattern(n - 1)
    print_numbers(n)
    print()


# 6. Reverse triangle
# 
def reverse_triangle(n):
    if n == 0:
        return
    line_stars(n)
    print()
    reverse_triangle(n - 1)


# 7. Multiplication table of n
def multiplication_table(n, i=1):
    if i > 10:
        return
    print(f"{n} x {i} = {n*i}")
    multiplication_table(n, i + 1)


# 8. Increasing + Decreasing

def inc_dec(n):
    if n == 0:
        return
    print(n, end=" ")
    inc_dec(n - 1)
    print(n, end=" ")


# 9. Sum of series with steps
def sum_series(n):
    if n == 1:
        print("1 =", 1)
        return 1
    result = n + sum_series(n - 1)
    print(f"{n} + ... =", result)
    return result


# 10. Character pattern (A, AB, ABC...)

def char_pattern(n, row=1):
    if row > n:
        return
    print_chars(row)
    print()
    char_pattern(n, row + 1)

def print_chars(n, char='A'):
    if n == 0:
        return
    print_chars(n - 1, char)
    print(chr(ord('A') + n - 1), end="")



# MAIN (Demo)

if __name__ == "__main__":
    n = 5

    print("1. Line of stars:")
    line_stars(n)
    print("\n")

    print("2. Square:")
    square_stars(n)
    print()

    print("3. Triangle Top Down:")
    triangle_top_down(n)
    print()

    print("4. Triangle Bottom Up:")
    triangle_bottom_up(n)
    print()

    print("5. Number Pattern:")
    number_pattern(n)
    print()

    print("6. Reverse Triangle:")
    reverse_triangle(n)
    print()

    print("7. Multiplication Table:")
    multiplication_table(5)
    print()

    print("8. Increasing & Decreasing:")
    inc_dec(n)
    print("\n")

    print("9. Sum of Series:")
    sum_series(n)
    print()

    print("10. Character Pattern:")
    char_pattern(n)