# Task 1
"""
Ask the user to enter an integer. Store the
value in x. Then add this code which counts
down
"""

x  = int(input("Enter an integer: "))
# use a while loop to print numbers until they are <0
while x > 0 :
    print(x)
    x-= 1

print("blastoff!!")

# Task 2

"""
Modify the loop to print out whether a
number is even or odd
"""

x  = int(input("Enter an integer: "))

while x > 0:
    # use modulo to see if the number divides by 2 evenly
    if x % 2 == 1:
        print(x, "is odd")
    else:
        print(x, "is even")
    x-= 1
print("blastoff!!")

#  Task 3
"""
Ask the user to enter in the amount of
decrease
"""
# ask for an integer
x  = int(input("Enter an integer: "))
# ask for the amount to decrease
d  = int(input("Enter decrease: "))
while x > 0:
    # use modulo to check if the number is even or odd
    if x % 2 == 1:
        print(x, "is odd")
    else:
        print(x, "is even")
    x-= d

# Task 4.1
"""
Write a different loop to print out
words until the word has a length less than
5 letters
"""
# run the loop until a condition breaks it
while True:
    word = input("Enter a word: ")
    print(word, f'has {len(word)} letters')
    if len(word)<5:
        print('goodbye')
        break

# Task 4.2
# set a variable to 0 and increment it inside the loop
entry  = 0
while entry < 5:
    word = input("Enter a word: ")
    print(f"{word}", f'has {len(word)} letters')
    # increment the variable by 1
    entry += 1
    # a False condition that will break our loop
    if len(word) < 5:
        print('goodbye')
        break
else:
    print('loser')

# Task 5
"""
Write a while loop that counts from 10
to 100 in decimal, binary, and hex
"""
a  = 10
while a < 101:
    print(a, bin(a), hex(a))
    a+=1

# Task 6
# Function using iteration
def stars_iter(num):
    while num > 0:
        # print '*' instead of the numbers
        print("*" * num)
        num-= 1
stars_iter(5)

# Function using recursion

def stars_recursion(num):
    print("*" * num)
    # base case
    if num == 0:
        return
    else:
        # call the function and decrease the argument by 1
        return stars_recursion(num - 1)
stars_recursion(7)

# Extra credit

"""
Write a recursive function in Python that
takes a positive integer as input and
returns the sum of its digits
"""
def sum_of_digits(num):
    # base case
    if len(str(num)) == 1:
        return num
    # turn the number into a string to iterate over digits using string slicing
    # and then turn it back into an int to add up the digits and get the sum
    return int(str(num)[0]) + sum_of_digits(int(str(num)[1:]))

print(sum_of_digits(7777))
"""
Write a recursive function that checks
whether a given string is a palindrome
"""
# Recursive Palindrome Check
def is_palindrome(w):

    def check_palindrome(word: str)-> bool:
# clean the users input argument, make sure it has no upper case letters or spaces
        cleaned_word = w.replace(" ", "").lower()
        # base case, the word is <=1 characters long
        if len(word) <=1:
            return True
        # check if the 1st and last letter are similar
        if cleaned_word[0]!= cleaned_word[-1]:
            return False
        # slice the string removing the first and last letter
        return check_palindrome(word[1:-1])

    if check_palindrome(w):
        print (f"{w} is a Palindrome")
    else:
        print(f"{w} is not a Palindrome")

is_palindrome('CAT')
is_palindrome('Bob  ' )
is_palindrome('LEVEL  ')
