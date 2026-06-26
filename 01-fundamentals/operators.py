# ============================================
# DAY 2: Operators + Input/Output
# ============================================

# --------------------------------------------
# 1. Arithmetic Operators
# --------------------------------------------
a = 10
b = 3

print("--- Arithmetic Operators ---")
print(a + b)    # Addition → 13
print(a - b)    # Subtraction → 7
print(a * b)    # Multiplication → 30
print(a / b)    # Division → 3.333... (always float)
print(a // b)   # Floor Division → 3 (decimal বাদ)
print(a % b)    # Modulus (ভাগশেষ) → 1
print(a ** b)   # Power → 1000 (10^3)


# --------------------------------------------
# 2. Comparison Operators
# --------------------------------------------
x = 10
y = 20

print("\n--- Comparison Operators ---")
print(x == y)   # False
print(x != y)   # True
print(x > y)    # False
print(x < y)    # True
print(x >= y)   # False
print(x <= y)   # True


# --------------------------------------------
# 3. Logical Operators
# --------------------------------------------
is_adult = True
has_id = False

print("\n--- Logical Operators ---")
print(is_adult and has_id)   # False
print(is_adult or has_id)    # True
print(not is_adult)          # False


# --------------------------------------------
# 4. input() + f-string formatting
# --------------------------------------------
print("\n--- Input/Output Demo ---")
name = input("What is your name? ")
print(f"Hello, {name}!")

age = int(input("What is your age? "))
print(f"Next year you'll be {age + 1}")


# ============================================
# PRACTICE QUESTIONS
# ============================================

# --------------------------------------------
# Q1: যোগ, বিয়োগ, গুণ, ভাগ
# --------------------------------------------
print("\n--- Q1: Basic Calculator ---")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)


# --------------------------------------------
# Q2: Even না Odd
# --------------------------------------------
print("\n--- Q2: Even or Odd ---")
num = int(input("Enter a number: "))
print(num % 2 == 0)   # True হলে even, False হলে odd


# --------------------------------------------
# Q3: Adult (18+) কিনা
# --------------------------------------------
print("\n--- Q3: Adult Check ---")
age = int(input("Enter your age: "))
print(age >= 18)


# --------------------------------------------
# Q4: Logical Operators Practice
# --------------------------------------------
print("\n--- Q4: Logical Operators ---")
print(5 > 3 and 10 > 8)    # True
print(5 > 10 or 10 > 8)    # True
print(not (5 > 10))        # True


# --------------------------------------------
# Q5: Simple Interest Calculator
# --------------------------------------------
print("\n--- Q5: Simple Interest Calculator ---")
principal = float(input("Enter Principal: "))
rate = float(input("Enter Rate (%): "))
time = float(input("Enter Time (years): "))

interest = (principal * rate * time) / 100
print(f"Simple Interest = {interest:.2f}")