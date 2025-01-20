# Python Control Flow
# =================

# Control flow helps us make decisions and repeat actions in our code

# 1. If Statements
# --------------
age = 18

print("If Statements:")
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Multiple conditions
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D")

# 2. For Loops
# -----------
print("\nFor Loops:")
# Loop through a list
fruits = ["apple", "banana", "orange"]
print("Fruits list:")
for fruit in fruits:
    print(fruit)

# Loop through a range
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)

# 3. While Loops
# ------------
print("\nWhile Loops:")
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

# Break and Continue
print("\nUsing break and continue:")
for i in range(5):
    if i == 2:
        continue  # Skip 2
    if i == 4:
        break    # Stop at 4
    print(i)

# 4. Try-Except (Error Handling)
# ----------------------------
print("\nError Handling:")
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("That's not a valid number!")

# Practice Exercises:
# 1. Write a program that checks if a number is positive, negative, or zero
# 2. Create a loop that prints the first 10 even numbers
# 3. Write a program that keeps asking for input until the user types 'quit'
# 4. Create a loop that sums all numbers from 1 to 100
# 5. Write a program that finds the largest number in a list
