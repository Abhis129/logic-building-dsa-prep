'''
PHASE 3 — RECURSION (THINKING IN SELF-REFERENCE)
Level 4: String-based Recursion

'''


# 1. Reverse a string using recursion.
def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]


# 2. Check if a string is palindrome using recursion.
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


# 3. Count vowels in a string recursively.
def count_vowels(s):
    if s == "":
        return 0
    vowels = "aeiouAEIOU"
    return (1 if s[0] in vowels else 0) + count_vowels(s[1:])


# 4. Remove all spaces from a string recursively.
def remove_spaces(s):
    if s == "":
        return ""
    if s[0] == " ":
        return remove_spaces(s[1:])
    return s[0] + remove_spaces(s[1:])


# 5. Replace all occurrences of a character (say ‘a’ → ‘x’) recursively.
def replace_char(s, old='a', new='x'):
    if s == "":
        return ""
    if s[0] == old:
        return new + replace_char(s[1:], old, new)
    return s[0] + replace_char(s[1:], old, new)


# 6. Remove all occurrences of a character from a string recursively.
def remove_char(s, ch):
    if s == "":
        return ""
    if s[0] == ch:
        return remove_char(s[1:], ch)
    return s[0] + remove_char(s[1:], ch)


# 7. Print all characters of a string one by one recursively.
def print_chars(s):
    if s == "":
        return
    print(s[0])
    print_chars(s[1:])


# 8. Print the string in reverse order recursively (without using loops).
def print_reverse(s):
    if s == "":
        return
    print_reverse(s[1:])
    print(s[0], end="")


# 9. Convert a string to uppercase recursively.
def to_uppercase(s):
    if s == "":
        return ""
    return s[0].upper() + to_uppercase(s[1:])


# 10. Count consonants and vowels separately using recursion.
def count_cv(s, v=0, c=0):
    if s == "":
        return v, c
    if s[0].isalpha():
        if s[0].lower() in "aeiou":
            return count_cv(s[1:], v+1, c)
        else:
            return count_cv(s[1:], v, c+1)
    return count_cv(s[1:], v, c)


# Demo
if __name__ == "__main__":
    s = "Abhishek Pandey"

    print("1:", reverse_string(s))
    print("2:", is_palindrome("madam"))
    print("3:", count_vowels(s))
    print("4:", remove_spaces(s))
    print("5:", replace_char(s, 'a', 'x'))
    print("6:", remove_char(s, 'a'))
    print("7:")
    print_chars(s)
    print("8:")
    print_reverse(s)
    print("\n9:", to_uppercase(s))
    print("10:", count_cv(s))