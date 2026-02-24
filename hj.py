from math import factorial

# Even or Odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

# Voting age
age = int(input("Enter your age: "))
if age >= 18:
    print("Congratulations, you can now exercise your right to vote.")
else:
    print(f"You cannot vote yet. You need to wait {18-age} more years.")

# Comparison
number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter a number: "))
if number_1 > number_2:
    print(f"{number_1} is greater than {number_2}.")
elif number_2 > number_1:
    print(f"{number_1} is less than {number_2}.")
else:
    print("The numbers are equal.")

# Even numbers list
print("The numbers in the list are: ")
for i in range(2, 101, 2):
    print(i)

# FizzBuzz Variation
for element in range(1, 100):
    if element % 3 == 0 and element % 5 == 0:
        print("I LOVE YOU")
    elif element % 3 == 0: 
        print("BABY") 
    elif element % 5 == 0:
        print("BUZZ")
    else:
        print(element)

# Multiplication Table
table_num = int(input("Enter a number: "))
print(f"The multiplication table for {table_num} is:")
for i in range(1, 11):
    print(f"{table_num} X {i} = {i * table_num}")

# Palindrome
word = input("Enter a word: ")
if word == word[::-1]:
    print(f"The word {word} is a palindrome.")
else:
    print(f"The word {word} is not a palindrome.")

# Prime Number
int_number = int(input("Enter an integer: "))
is_prime = True
if int_number < 2: is_prime = False
for i in range(2, int(int_number ** 0.5) + 1):
    if int_number % i == 0:
       is_prime = False
       break
if is_prime:
    print("The number is prime.")
else:
    print("The number is not prime.")

# Factorial
factor = int(input("Enter a number to calculate its factorial: "))
result = factorial(factor)
print(result) 

# Clothing sizes
pants_size = int(input("Enter your pants size: "))
shirt_size = int(input("Enter your shirt size: "))
print(f"\n\t[Pants]: Your pants size is: {pants_size}.")
print(f"\n\t[Shirt]: Your shirt size is: {shirt_size}.")

# Sum of 10 numbers
total_sum = 0
for i in range(10):
    num_to_sum = float(input("Enter a number: "))
    total_sum += num_to_sum
    print(f"The current sum of the entered numbers is {total_sum}")

