# 1 String operations create a new string
# based on the first
"""
user_word = input("Enter a word/phrase: ")
user_word2 = input("Enter the word/phrase in upper case: ")
if user_word2 == user_word.upper():
    print("Stop shouting please!")
"""
"""
# 2 Count the number of different vowels in a string
vowels = ["a", "o", "i", "u", "e"]
num_of_vowels = 0
user_input = input("Enter a word/phrase: ")

for vowel in user_input:
    if vowel in vowels:
        num_of_vowels += 1
print(f"{user_input} has {num_of_vowels} vowels.")
"""

# 3 Write code that asks the user to enter two
# strings
user_string1 = input("Enter a string: ")
user_string2 = input("Enter a string: ")

if user_string1 > user_string2:
    print(user_string1)
else:
    print(user_string2)

# 4 # Ask a user to enter their email

email_1 = input("Enter your email address: ")
email_2 = input("Enter your email address again: ")

if email_2 != email_1:
    print("The two inputs did not match.")
elif email_2 == email_1:
    print("Thank you!")

# 5 Write two functions that will print the
# factorial of a number. Make one function
# iterative and one recursive

# iteration
import time

def Factorial(x):
    total = 1
    for number in range (1, x+1):
        total*= number
    return total
print(Factorial(4))
start_time = time.time()
print(f"Iterative Factorial: {Factorial(4)}")
end_time = time.time()
print(f"Time taken (iterative): {end_time - start_time:.10f} seconds")

# recursion
def factorial(x):
    # base case
    if x == 1:
        return 1

    return x * factorial(x - 1)

start_time = time.time()
print(f"Recursive Factorial: {factorial(4)}")
end_time = time.time()
print(f"Time taken (recursive): {end_time - start_time:.10f} seconds")

