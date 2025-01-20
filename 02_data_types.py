# Python Data Types
# ===============

# In this lesson, we'll learn about different data types in Python

# 1. Numbers
# ---------
integer_number = 42        # Integer
float_number = 3.14       # Float (decimal)

print("Numbers:")
print("Integer:", integer_number)
print("Float:", float_number)

# 2. Strings
# ---------
# Strings are text enclosed in quotes
single_quoted = 'Hello'
double_quoted = "World"
multi_line = '''This is a
multi-line
string'''

print("\nStrings:")
print(single_quoted + " " + double_quoted)
print("Length of 'Hello':", len(single_quoted))
print("Uppercase:", single_quoted.upper())
print("Lowercase:", double_quoted.lower())

# 3. Lists
# -------
# Lists are ordered collections of items
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed_list = ["hello", 42, 3.14, True]

print("\nLists:")
print("Fruits:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
fruits.append("grape")
print("After adding grape:", fruits)

# 4. Tuples
# --------
# Tuples are immutable (unchangeable) lists
coordinates = (10, 20)
rgb_color = (255, 128, 0)

print("\nTuples:")
print("Coordinates:", coordinates)
print("X coordinate:", coordinates[0])
print("Y coordinate:", coordinates[1])

# 5. Dictionaries
# -------------
# Dictionaries store key-value pairs
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print("\nDictionaries:")
print("Person:", person)
print("Name:", person["name"])
print("Age:", person["age"])

# 6. Boolean
# ---------
# Boolean values are either True or False
is_sunny = True
is_raining = False

print("\nBoolean:")
print("Is it sunny?", is_sunny)
print("Is it raining?", is_raining)

# Practice Exercises:
# 1. Create a list of your favorite colors
# 2. Create a dictionary about your favorite movie (title, year, director)
# 3. Create a tuple with your birth date (day, month, year)
# 4. Try to modify a tuple and observe what happens
# 5. Create a list and try different list methods (append, remove, sort)
