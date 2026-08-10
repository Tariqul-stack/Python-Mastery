# ============================================
# DAY 11: Functions — Basics
# ============================================

# --------------------------------------------
# 1. Basic Function Syntax
# --------------------------------------------
print("--- Basic Function ---")

def greet(name):
    print(f"Hello, {name}!")
    print("Welcome to Python!")

greet("Rahim")
greet("Karim")


# --------------------------------------------
# 2. Parameters + Return
# --------------------------------------------
print("\n--- Parameters + Return ---")

def add(a, b):
    return a + b

result = add(10, 20)
print(result)                  # 30
print(add(5, 3) * 2)          # 16


# --------------------------------------------
# 3. Multiple Return Values
# --------------------------------------------
print("\n--- Multiple Return Values ---")

def min_max(numbers):
    return min(numbers), max(numbers)

smallest, largest = min_max([3, 1, 4, 1, 5, 9])
print(f"Min: {smallest}, Max: {largest}")


# --------------------------------------------
# 4. Default Arguments
# --------------------------------------------
print("\n--- Default Arguments ---")

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Tariqul")                        # default ব্যবহার
greet("Tariqul", "Hi")                  # override করা
greet("Tariqul", "Assalamu Alaikum")    # custom greeting


# --------------------------------------------
# 5. Keyword Arguments
# --------------------------------------------
print("\n--- Keyword Arguments ---")

def student_info(name, age, city):
    print(f"{name}, {age}, {city}")

student_info("Tariqul", 21, "Dhaka")                    # positional
student_info(age=21, city="Dhaka", name="Tariqul")      # keyword
student_info("Tariqul", city="Dhaka", age=21)           # mixed


# --------------------------------------------
# 6. Docstring
# --------------------------------------------
print("\n--- Docstring ---")

def add_with_doc(a, b):
    """
    দুটো সংখ্যা যোগ করে।

    Parameters:
        a: প্রথম সংখ্যা
        b: দ্বিতীয় সংখ্যা

    Returns:
        দুটো সংখ্যার যোগফল
    """
    return a + b

print(add_with_doc(3, 4))
print(add_with_doc.__doc__)


# --------------------------------------------
# 7. Function calling Function
# --------------------------------------------
print("\n--- Function Inside Function ---")

def square(n):
    return n ** 2

def sum_of_squares(a, b):
    return square(a) + square(b)

print(sum_of_squares(3, 4))    # 9 + 16 = 25


# ============================================
# PRACTICE QUESTIONS
# ============================================

# --------------------------------------------
# Q1: Basic Calculator Functions
# --------------------------------------------
print("\n--- Q1: Calculator Functions ---")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition:       {add(num1, num2)}")
print(f"Subtraction:    {subtract(num1, num2)}")
print(f"Multiplication: {multiply(num1, num2)}")
print(f"Division:       {divide(num1, num2)}")


# --------------------------------------------
# Q2: Grade Function
# --------------------------------------------
print("\n--- Q2: Grade Function ---")

def get_grade(marks):
    """marks নিয়ে grade return করে"""
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

marks_list = [95, 82, 74, 65, 45]
for mark in marks_list:
    print(f"Marks: {mark} → Grade: {get_grade(mark)}")


# --------------------------------------------
# Q3: String Utilities
# --------------------------------------------
print("\n--- Q3: String Utilities ---")

def is_palindrome(word):
    """word টা palindrome কিনা True/False return করে"""
    return word == word[::-1]

def count_vowels(text):
    """text এ কতটা vowel আছে সেটা return করে"""
    count = 0
    vowels = "aeiou"
    for char in text.lower():    # lowercase করে uppercase miss হয় না
        if char in vowels:
            count += 1
    return count

def reverse_words(sentence):
    """sentence এর words উল্টো order এ return করে"""
    words = sentence.split()
    words.reverse()
    return " ".join(words)

print(is_palindrome("madam"))           # True
print(is_palindrome("hello"))           # False
print(count_vowels("Hello World"))      # 3
print(reverse_words("Hello World"))     # World Hello


# --------------------------------------------
# Q4: Temperature Converter
# --------------------------------------------
print("\n--- Q4: Temperature Converter ---")

def celsius_to_fahrenheit(c):
    """Celsius থেকে Fahrenheit এ convert করে"""
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    """Fahrenheit থেকে Celsius এ convert করে"""
    return (f - 32) * 5/9

print("Type 'C' to convert Celsius → Fahrenheit")
print("Type 'F' to convert Fahrenheit → Celsius")
direction = input("Your choice: ").upper()   # uppercase normalize
temperature = float(input("Enter temperature: "))

if direction == "C":
    result = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C = {result:.2f}°F")
elif direction == "F":
    result = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F = {result:.2f}°C")
else:
    print("Invalid direction!")


# --------------------------------------------
# Q5: Simple ATM
# --------------------------------------------
print("\n--- Q5: Simple ATM ---")

def atm(balance=5000, amount=0, transaction_type=""):
    """
    ATM transaction handle করে।

    Parameters:
        balance: বর্তমান balance (default 5000)
        amount: transaction এর পরিমাণ
        transaction_type: 'deposit' বা 'withdraw'

    Returns:
        নতুন balance অথবা error message
    """
    if transaction_type == "deposit":
        return balance + amount
    elif transaction_type == "withdraw":
        if amount > balance:
            return "Insufficient funds"
        return balance - amount
    else:
        return "Invalid transaction"

# Test cases
print(atm(5000, 1000, "deposit"))    # 6000
print(atm(5000, 2000, "withdraw"))   # 3000
print(atm(5000, 7000, "withdraw"))   # Insufficient funds
print(atm(5000, 500,  "transfer"))   # Invalid transaction