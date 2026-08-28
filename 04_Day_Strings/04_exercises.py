# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

list_of_words = ['Thirty', 'Days', 'Of', 'Python']
# print(" ".join(list_of_words))

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

list_of_words = ['Coding', 'For', 'All']
single_string = " ".join(list_of_words)
# print(single_string)

# Declare a variable named company and assign it to an initial value "Coding For All".

company = "Coding For All"

# Print the variable company using print().

print(company)

# Print the length of the company string using len() method and print().

print(len(company))

# Change all the characters to uppercase letters using upper() method.

print(company.upper())

# Change all the characters to lowercase letters using lower() method.

print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.

print(company[7:])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.

word = 'Coding For All'
print(word.index('Coding')) 
print(word.find('Coding'))
print('Coding' in word)

# Replace the word coding in the string 'Coding For All' to Python.

word = 'Coding For All'
print(word.replace('Coding', 'Python'))

# Change "Python for Everyone" to "Python for All" using the replace method or other methods.

word = 'Python for Everyone'
print(word.replace('Everyone', 'All'))

# Split the string 'Coding For All' using space as the separator (split()) .

word = 'Coding For All'
print(word.split(' '))

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

word = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(word.split(','))

# What is the character at index 0 in the string Coding For All.

word = 'Coding For All'
print(word[0])

# What is the last index of the string Coding For All.

word = 'Coding For All'
print(word[-1])

# What character is at index 10 in "Coding For All" string.

word = 'Coding For All'
print(word[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.

target_word = 'Python For Everyone'
acronym = ''.join(word[0] for word in target_word.split()).upper()
print(acronym)

# Create an acronym or an abbreviation for the name 'Coding For All'.

target_word = 'Coding For All'
acronym = ''.join(word[0] for word in target_word.split()).upper()
print(acronym)

# Use index to determine the position of the first occurrence of C in Coding For All.
# Use index to determine the position of the first occurrence of F in Coding For All.

word = 'Coding For All'
print(word.index('C'))
print(word.index('F'))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.

word = 'Coding For All People'
print(word.rfind('l'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Does 'Coding For All' start with a substring Coding?
# Does 'Coding For All' end with a substring coding?
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki

# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.

# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144