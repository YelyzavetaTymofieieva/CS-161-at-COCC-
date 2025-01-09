# Task 1: Print your pet’s type and name using an f-String.

pet_type = 'dog'
pet_name  = 'Ursa'
print(f"I have a {pet_type} and her name is {pet_name}.")

# Task 2: Use input statements to take input and an f-String to print the results as shown
f_name = input("Enter your first name: ")
age = int(input("Enter your age: "))
savings = int(input("Enter your yearly savings: "))
print(f"Hello {f_name}! You are currently {age} years old.")
print(f"In 10 years, you will be {age+10} years old.")
print(f"If you save ${savings} each year, in 5 years you will have saved ${savings*5}.")

# Task 3: Use an f-String to print out the number of seconds in the current month.

from datetime import datetime
first_day = datetime(2025, 1, 1)
last_day = datetime(2025, 2, 1)

num_of_days = last_day - first_day
num_of_seconds = int(num_of_days.total_seconds())

print(f"The number of seconds in January is {num_of_seconds}")

# Task 4: Use the // operator for integer division and % for the integer remainder.

number_of_eggs = int(input("Enter the number of eggs: "))
print(f"This makes {number_of_eggs // 12} dozen eggs and {number_of_eggs % 12} left over.")