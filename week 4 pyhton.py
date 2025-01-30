# Task 1

def avg (x,y,z):
    mean = (x+y+z)/3
    return mean
print(f"The average is: {avg(150,93,33)}")

# Task 2
# The script won't run and
# there will be an error message saying
# "NameError: name 'avg' is not defined" because we
# define the function
# after calling it

#Task 3
# The script will return the average of the numbers but won't return
# the value of the variable showing an error message "NameError: name 'x' is not defined"
# because the x is not defined outside the function

# Task 4
# define a function to calculate dog's human age
def calculate_age(number):
    human_age = 24+(number - 2)*4
    return f"{number} dog years is equivalent to {human_age} human years."
dog_age = int(input("Enter your dog's age: "))
print(calculate_age(dog_age))

# Task 5
# define a function with 3 variables
def calculate_price(car_price, n_years, car_type):
    if car_type == "German" or car_type == "Italian":
        # calculate the price after depreciation
        new_price = round(car_price*(( 1 - 0.05)**n_years))
    elif car_type == "Japanese":
        new_price = round(car_price*((1 - 0.07)**n_years))
    # write a condition that will return error in case a user inputs an incorrect car type
    else:
        print ("Error, wrong car type. Re-enter.")
    return f"The value of a {car_type} car will be ${new_price} after {n_years} years."

# user input values
price = int(input("Enter your car's price: "))
age = int(input("Enter your car's age: "))
car = input("Enter your car's type (German, Japanese or Italian):").capitalize()

# call the function and print the result
print(calculate_price(price, age, car))

#Task 6

# define a function to calculate dog's human age
def calculate_age(num):
    return 24+(num - 2)*4
# we use input outside the function
dog_name = input("What is your dog’s name? ")
dog_age = int(input("Enter your dog's age: "))

# use f-string to return the dog's name and age, calculated by the function above
print(f"Your {dog_name.capitalize()} is {calculate_age(dog_age)} human years old.")

# Task 7
# define a function
def calculate_price(num):
    # return a number, the calculated price
    return round(num * 1.15 + 2.25, 3)
# user input
scoops = int(input("Ice cream cone price calculator: \n How many scoops would you like? "))
print(f"A {scoops}-scoop cone will cost ${calculate_price(scoops)}.")