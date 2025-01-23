#1 Ask the user to enter their name

user_name = input("Please, enter your name: ")
print(f"Hello, {user_name}")

# 2 Ask the user to input their age
user_age = int(input("Please, enter your age: "))
print(user_age + 5)

# The error message says: "can only concatenate str (not "int") to str"
# this means that we are trying to concatenate two different data types,
# an integer 5 and a string (user input). To fix that, we have to change the user's input

# 3 Ask the user to input how many years to add to their age
years_to_add = int(input("How many years do you want to add to your age? "))
print(f"In {years_to_add} years you will be {user_age + years_to_add} years old.")

# Extra credit

from datetime import date

# User input
dob = int(input("Enter your year of birth: "))
gender = input("Enter your gender (M/F): ")

def death_date(dob, gender):

    # Average life expectancy
    average_life_expectancy = {'M': 73.54, 'F': 79.30}
    # Calculate user's current age
    today = date.today()
    current_age = today.year - dob

    # Check the user's gender and calculate the expected year of death
    if gender in average_life_expectancy:
        remaining_years = round(average_life_expectancy[gender] - current_age)
        expected_year_of_death = round(today.year + remaining_years)
        return f"Expected year of death: {expected_year_of_death}. You are expected to live approximately {remaining_years} more years."
    else:
        return "Invalid gender. Please enter 'male' or 'female'."

# Calculate and display the result
result = death_date(dob, gender)
print(result)


# 4 Ask the user to enter values that might be floating point

hours = float(input("Enter the number of hours worked: "))
h_wage = float(input("Enter your hourly wage, without the $: "))

# Calculate weekly and annual income
weekly_pay = round(hours * h_wage, 2)
annual_income = round(weekly_pay * 50)  # Assume there are 50 working weeks in a year

# Print the results
print(f"Your gross pay this week is ${weekly_pay}. Your estimated annual gross pay will be ${annual_income}.")

income_level = [11600.00, 47150.00, 100525.00, 191950.00, 243725.00, 609350.00, 609350.01]
tax_rate = [10, 12, 22, 24, 32, 35, 37]

# Iterate through the list of income levels
for i in range(len(income_level) - 1):
    if income_level[i] <= annual_income < income_level[i + 1]:
        rate = tax_rate[i] / 100  # get the tax rate according to your income
        tax = annual_income * rate  # Calculate the tax amount
        print(f"Your tax rate is {tax_rate[i]}%, and your tax amount is ${tax}.")

    # an elif condition in case annual income is lower than the first threshold 11,600.00
    elif annual_income < 11600.00:
        rate = 0.1
        tax = annual_income * rate
        print(f"Your tax rate is 10%, and your tax amount is ${tax}.")
        break
    else:
        print("Your income does not fall within the expected tax brackets.")