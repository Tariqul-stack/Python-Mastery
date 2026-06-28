# ============================================
# DAY 3: Conditionals (if/elif/else)
# ============================================

# --------------------------------------------
# 1. Basic if statement
# --------------------------------------------
print("--- Basic if ---")
age = 20

if age >= 18:
    print("You are an adult")


# --------------------------------------------
# 2. if-else
# --------------------------------------------
print("\n--- if-else ---")
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")


# --------------------------------------------
# 3. if-elif-else (Multiple Conditions)
# --------------------------------------------
print("\n--- if-elif-else ---")
marks = 75

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")


# --------------------------------------------
# 4. Nested Conditionals
# --------------------------------------------
print("\n--- Nested if ---")
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("Can drive")
    else:
        print("Need a license first")
else:
    print("Too young to drive")


# --------------------------------------------
# 5. Logical Operators with Conditionals
# --------------------------------------------
print("\n--- Logical Operators in if ---")
age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")


# ============================================
# PRACTICE QUESTIONS
# ============================================

# --------------------------------------------
# Q1: Grade Calculator
# --------------------------------------------
print("\n--- Q1: Grade Calculator ---")
marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")


# --------------------------------------------
# Q2: Even/Odd Checker
# --------------------------------------------
print("\n--- Q2: Even/Odd Checker ---")
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# --------------------------------------------
# Q3: Largest of 3 Numbers
# --------------------------------------------
print("\n--- Q3: Largest of 3 Numbers ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is: {largest}")


# --------------------------------------------
# Q4: Login System (Simplified)
# --------------------------------------------
print("\n--- Q4: Login System ---")
correct_username = "admin"
correct_password = "1234"

username_input = input("Enter username: ")
password_input = input("Enter password: ")

if username_input == correct_username and password_input == correct_password:
    print("Login successful")
else:
    print("Login failed")


# --------------------------------------------
# Q5: Leap Year Checker
# --------------------------------------------
print("\n--- Q5: Leap Year Checker ---")
year = int(input("Enter a year: "))

# (৪ দিয়ে ভাগ যাবে এবং ১০০ দিয়ে যাবে না) অথবা (৪০০ দিয়ে ভাগ যাবে)
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")