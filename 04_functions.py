# Python Functions
# ===============

# Functions are reusable blocks of code that perform specific tasks

# 1. Basic Function
# ---------------
def greet():
    print("Hello, World!")

print("Basic function:")
greet()

# 2. Function with Parameters
# ------------------------
def greet_person(name):
    print(f"Hello, {name}!")

print("\nFunction with parameters:")
greet_person("Alice")

# 3. Function with Return Value
# --------------------------
def add_numbers(a, b):
    return a + b

print("\nFunction with return value:")
result = add_numbers(5, 3)
print("5 + 3 =", result)

# 4. Default Parameters
# ------------------
def greet_with_title(name, title="Mr."):
    print(f"Hello, {title} {name}")

print("\nDefault parameters:")
greet_with_title("Smith")
greet_with_title("Johnson", "Dr.")

# 5. Multiple Parameters
# -------------------
def calculate_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

print("\nMultiple return values:")
area, perimeter = calculate_rectangle(4, 5)
print(f"Rectangle area: {area}")
print(f"Rectangle perimeter: {perimeter}")

# 6. Lambda Functions (Anonymous Functions)
# -------------------------------------
square = lambda x: x * x

print("\nLambda function:")
print("Square of 5:", square(5))

# 7. Function with *args (Variable Arguments)
# ---------------------------------------
def sum_all(*numbers):
    return sum(numbers)

print("\nVariable arguments:")
print("Sum:", sum_all(1, 2, 3, 4, 5))

# 8. Function with **kwargs (Keyword Arguments)
# ----------------------------------------
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\nKeyword arguments:")
print_info(name="John", age=30, city="New York")

# Practice Exercises:
# 1. Write a function that returns the maximum of three numbers
# 2. Create a function that converts temperature from Celsius to Fahrenheit
# 3. Write a function that counts the number of vowels in a string
# 4. Create a function that generates a list of even numbers up to a given number
# 5. Write a function that checks if a number is prime
