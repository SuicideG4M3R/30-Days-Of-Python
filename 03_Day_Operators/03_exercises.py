# Declare your age as integer variable

age = int(25)

# Declare your height as a float variable

height = float(5.11)

# Declare a variable that store a complex number

complex_num = complex(3 + 1j)

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100

user_base = float(input("Enter base: "))
user_height = float(input("Enter height: "))
area = 0.5 * user_base * user_height

print(f"The area of the triangle is {area}")
 
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12

user_side_a = float(input("Enter side A: "))
user_side_b = float(input("Enter side B: "))
user_side_c = float(input("Enter side C: "))
user_perimeter = user_side_a + user_side_b + user_side_c

print(f"Perimeter of your triangle is: {user_perimeter}")

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

user_lenght_of_rectangle = float(input("Enter rectangle lenght: "))
user_width_of_rectangle = float(input("Enter rectangle width: "))
area = user_lenght_of_rectangle * user_width_of_rectangle
perimeter = 2 * (user_lenght_of_rectangle + user_width_of_rectangle)

print(f"Your rectangle area is {area}, and perimeter is {perimeter}")

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

user_radius = float(input("Enter radius of a circle: "))

print(f"Area = {3.14 * user_radius * user_radius}\nCircumference = {2 * 3.14 * user_radius}")

# Calculate the slope, x-intercept and y-intercept of y = 2x -2



# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Compare the slopes in tasks 8 and 9.




# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
# There is no 'on' in both dragon and python
# Find the length of the text python and convert the value to float and convert it to string
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# Check if type of '10' is equal to type of 10
# Check if int('9.8') is equal to 10
# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125