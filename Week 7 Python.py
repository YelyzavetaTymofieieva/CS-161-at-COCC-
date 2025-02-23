# 1. Write a while loop that prints out all the even numbers between two numbers that the user inputs

input_1 = int(input("Enter the first number: "))
input_2 = int(input("Enter the second number: "))

for n in range(input_1, input_2):
    if n % 2 ==0:
        print(n)

# 2. Write a while loop that prints out all the factors of a given positive integer

user_number = int(input("Enter a positive integer: ")) # Get input from the user
num = 1 # Start checking from 1

while num <= user_number:
    if user_number % num == 0:  # Check if num is a factor
        print(num)

    # Increment to check the next number
    num += 1


# 3. Loop Iteration

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
name = input("Enter name: ").lower() # take the user's input
# In initialize the total of indexes
total = 0

# loop through the characters in the input string
for char in name:
# check if the character is on the alphabet list
    if char in alphabet:
# if the char is on the list, return its index and add to the total
        total+= alphabet.index(char)
print(total)


# 4. Recursion
def square(number):
    # base case
    if number == 1:
        print(1)
    else:
        square(number-1)
        print(number**2)

#square(5)

# 5. TeePee Sort
unsorted_list = (12, 43, 22, 34, 2, 21, 3, 33, 81)

def teepee_sort(unsorted_lst):
    # create a list of odd num
    odd_num = sorted([num for num in unsorted_lst if num % 2 == 1])
    # create a list of even num
    even_num = sorted([num for num in unsorted_lst if num % 2 == 0])
    # find the largest num in the unsorted_list
    largest_num = max(unsorted_list)

    # remove the largest num from either of the lists it is in
    # to concatenate it to the middle final sorted list

    if largest_num in odd_num:
        odd_num.remove(largest_num)
    else:
        even_num.remove(largest_num)
    return odd_num + [largest_num] + even_num
sorted_list = teepee_sort(unsorted_list)
#print(sorted_list)


# 6. Find the next Highest Number
def rearrange(x):
    digits = list(str(x))
    length = len(digits)
    # find the second last index
    indx = length - 2
    while indx >= 0 and digits[indx] >= digits[indx + 1]:
        indx -= 1

    if indx == -1:
        return ("No larger arrangement is possible")

    # the last digit index len - 1 because we start indexing with 0
    l = length -1
    while digits[l] <= digits[indx]:
        l-= 1
    digits[indx], digits[l] = digits[l], digits[indx]
    digits = digits[:indx + 1] + sorted(digits[indx + 1:])
    next_number = int("".join(digits))
    print(next_number)
    # call the function recursively until we run out of possible larger arrangements
    return rearrange(next_number)
#print(rearrange("450"))



