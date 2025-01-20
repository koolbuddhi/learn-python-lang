# Advanced Array Manipulation in Python
# ================================

# List/Array Slicing
# -----------------
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Original list:", numbers)

# Basic slicing [start:end:step]
print("\nBasic Slicing:")
print("First 3 elements ([:3]):", numbers[:3])        # [0, 1, 2]
print("Elements 3 to 6 ([3:6]):", numbers[3:6])      # [3, 4, 5]
print("Last 3 elements ([-3:]):", numbers[-3:])      # [7, 8, 9]
print("Every second element ([::2]):", numbers[::2])  # [0, 2, 4, 6, 8]

# Negative stepping
print("\nReverse Slicing:")
print("Reverse list ([::-1]):", numbers[::-1])       # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print("Last 3 elements reversed ([-1:-4:-1]):", numbers[-1:-4:-1])  # [9, 8, 7]

# Array Operations
# --------------
import numpy as np

# Creating numpy arrays
arr = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("\nNumPy Array Operations:")
print("Original array:", arr)
print("2D array:\n", arr_2d)

# Array slicing
print("\nArray Slicing:")
print("First 2 rows of 2D array:", arr_2d[:2])
print("First column:", arr_2d[:, 0])  # All rows, first column
print("Diagonal elements:", np.diagonal(arr_2d))

# Advanced Operations
# ----------------
print("\nAdvanced Operations:")

# List comprehension with slicing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers[::2] if x % 2 == 0]
print("Even numbers using slice and comprehension:", even_numbers)

# Multiple slicing
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
submatrix = [row[1:] for row in matrix[:2]]
print("Submatrix using multiple slicing:", submatrix)

# Slice assignment
numbers = [0, 1, 2, 3, 4, 5]
numbers[1:4] = [10, 20, 30]
print("After slice assignment:", numbers)

# Practical Examples
# ---------------
def get_middle_third(lst):
    """Get the middle third of a list."""
    size = len(lst)
    start = size // 3
    end = 2 * (size // 3)
    return lst[start:end]

sample = list(range(12))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("\nPractical Examples:")
print("Middle third:", get_middle_third(sample))

# Working with strings (strings are also sequences)
text = "Python Programming"
print("String slicing:")
print("First word:", text[:6])
print("Reverse string:", text[::-1])

# Practice Exercises:
# 1. Create a function that rotates a list by n positions using slicing
# 2. Extract alternate elements from a 2D numpy array
# 3. Write a function that returns the last n elements of a list in reverse order
# 4. Create a function that extracts a spiral pattern from a 2D matrix using slicing
