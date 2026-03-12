# 1. Take a number and print whether it’s positive, negative, or zero.

# num = int(input("Enter a number: "))

# if num == 0:
#     print("Zero")
# elif num > 0:
#     print("Postive")
# else:
#     print("Negative")

# 2. Check if a number is even or odd.
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# 3. Check if a number is divisible by 5.
# num = int(input("Enter a number: "))
# if num % 5 == 0:
#     print("Divisible by 5")
# else:
#     print("Not Divisible by 5")

# 4. Check if a number is divisible by both 3 and 5.
# num = int(input("Enter a number: "))
# if num % 3 == 0 and num % 5 == 0:
#     # if num % 5 == 0:
#     print("Divisible by 3 and 5")
# else:
#     print("Not Divisible by 5")


# 5. Check if a given year is a leap year.


# 6. Take two numbers and print the larger one.
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a 2nd number: "))

# if num1 < num2:
#     print(num2, "is the largest number.")
# else:
#     print(num1, "is the latgest number")

# 7. Take three numbers and print the largest.
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a 2nd number: "))
# num3 = int(input("Enter a 3rd number: "))

# if num1 >= num2 and num1 >= num3:
#     print(num1)
# elif num2 >= num1 and num2 >= num3:
#     print(num2)
# else:
#     print(num3)

# 8. Take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions.

# temp = float(input("What is the temperature: "))

# if 40 <= temp <= 100:
#     print("HOT")

# elif 20 <= temp <=39:
#     print("WARM")

# else:
#     print("COLD")

# 9. Take a character and check if it’s a vowel or consonant.

a = input("Enter an alphabet: ").upper()

if a not in ['A','E', 'I', 'O', 'U']:
    # print(a, "is a vowel")
    print(a,"is a consonant")
else: 
    # print(a,"is a consonant")
    print(a, "is a vowel")
# 10. Take a character and check whether it’s uppercase, lowercase, a digit, or a special
# character.