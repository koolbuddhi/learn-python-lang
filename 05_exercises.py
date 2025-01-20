# Python Practice Exercises
# =====================

# Here are some exercises to practice what you've learned
# Try to solve these exercises on your own first, then check the solutions

# Exercise 1: Temperature Converter
# ------------------------------
def celsius_to_fahrenheit(celsius):
    # TODO: Write code to convert Celsius to Fahrenheit
    # Formula: (celsius * 9/5) + 32
    pass

# Test Exercise 1
# print(celsius_to_fahrenheit(0))    # Should print 32.0
# print(celsius_to_fahrenheit(100))  # Should print 212.0

# Exercise 2: List Operations
# ------------------------
def find_largest_number(numbers):
    # TODO: Find and return the largest number in the list
    pass

# Test Exercise 2
# numbers = [5, 2, 9, 1, 7, 6, 3]
# print(find_largest_number(numbers))  # Should print 9

# Exercise 3: String Manipulation
# ---------------------------
def count_vowels(text):
    # TODO: Count and return the number of vowels in the text
    # Vowels are: a, e, i, o, u (both lowercase and uppercase)
    pass

# Test Exercise 3
# print(count_vowels("Hello World"))  # Should print 3
# print(count_vowels("Python"))       # Should print 1

# Exercise 4: Dictionary Operations
# -----------------------------
def create_grade_book(names, scores):
    # TODO: Create and return a dictionary where names are keys and scores are values
    pass

# Test Exercise 4
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]
# print(create_grade_book(names, scores))

# Exercise 5: Prime Number Checker
# ----------------------------
def is_prime(number):
    # TODO: Check if the number is prime
    # A prime number is only divisible by 1 and itself
    pass

# Test Exercise 5
# print(is_prime(7))    # Should print True
# print(is_prime(12))   # Should print False

# Solutions are commented out. Try to solve the exercises first!
# Uncomment the solution to check your answer

"""
# Solution 1: Temperature Converter
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Solution 2: List Operations
def find_largest_number(numbers):
    return max(numbers)

# Solution 3: String Manipulation
def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

# Solution 4: Dictionary Operations
def create_grade_book(names, scores):
    return dict(zip(names, scores))

# Solution 5: Prime Number Checker
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
"""

# Additional Challenges:
# 1. Modify the temperature converter to also convert Fahrenheit to Celsius
# 2. Add error handling to the exercises
# 3. Create more test cases for each function
# 4. Try to solve the exercises using different approaches
# 5. Create your own exercises and solve them!
