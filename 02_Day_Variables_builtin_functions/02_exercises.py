# Exercises: Level 1
# Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
# Write a python comment saying 'Day 2: 30 Days of python programming'

from encodings import undefined


print("Day 2: 30 Days of python programming")

# Declare a first name variable and assign a value to it

first_name = "Robert"

# Declare a last name variable and assign a value to it

last_name = "Szczepanski"

# Declare a full name variable and assign a value to it

full_name = f"{first_name} {last_name}"

# Declare a country variable and assign a value to it

country = "Poland"

# Declare a city variable and assign a value to it

city = "Warsaw"

# Declare an age variable and assign a value to it

age = 24

# Declare a year variable and assign a value to it

current_year = 2026

# Declare a variable is_married and assign a value to it

is_married = True

# Declare a variable is_true and assign a value to it

is_true = True

# Declare a variable is_light_on and assign a value to it

is_light_on = False

# Declare multiple variable on one line

is_employed, has_children, has_superpowers = True, False, undefined

# Exercises: Level 2
# Check the data type of all your variables using type() built-in function

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(current_year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(is_employed))
print(type(has_children))
print(type(has_superpowers))

# Using the len() built-in function, find the length of your first name

print(len(first_name))

# Compare the length of your first name and your last name

print(len(first_name) == len(last_name))

# Declare 5 as num_one and 4 as num_two

num_one = 5
num_two = 4

# Add num_one and num_two and assign the value to a variable total

total = num_one + num_two
print(total)

# Subtract num_two from num_one and assign the value to a variable diff

diff = num_one - num_two
print(diff)

# Multiply num_two and num_one and assign the value to a variable product

product = num_one * num_two
print(product)

# Divide num_one by num_two and assign the value to a variable division

division = num_one / num_two
print(division)

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder

remainder = num_two % num_one
print(remainder)

# Calculate num_one to the power of num_two and assign the value to a variable exp

exp = num_one ** num_two
print(exp)

# Find floor division of num_one by num_two and assign the value to a variable floor_division

floor_division = num_one // num_two
print(floor_division)

# The radius of a circle is 30 meters.
radius_of_circle = 30
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = 3.14 * radius_of_circle ** 2
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * 3.14 * radius_of_circle
# Take radius as user input and calculate the area.
user_radius = float(input("Enter the radius of the circle: "))
user_area = 3.14 * user_radius ** 2
print(f"The area of the circle with radius {user_radius} is: {user_area}")
# Use the built-in input function to get first name, last name, country and ag2e from a user and store the value to their corresponding variable 

user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_country = input("Enter your country: ")
user_age = int(input("Enter your age: "))

print(f"User's full name is: {user_first_name} {user_last_name}, from {user_country}, aged {user_age}.")

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords