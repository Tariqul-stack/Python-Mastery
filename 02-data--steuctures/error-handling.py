# ============================================
# DAY 13: Error Handling
# ============================================

# --------------------------------------------
# 1. Basic try/except
# --------------------------------------------
print("--- Basic try/except ---")
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")


# --------------------------------------------
# 2. Common Exceptions
# --------------------------------------------
print("\n--- Common Exceptions ---")

try:
    x = [1, 2, 3]
    print(x[10])
except IndexError as e:
    print(f"IndexError: {e}")

try:
    d = {"name": "Tariqul"}
    print(d["age"])
except KeyError as e:
    print(f"KeyError: {e}")

try:
    print("hello" + 5)
except TypeError as e:
    print(f"TypeError: {e}")


# --------------------------------------------
# 3. else + finally
# --------------------------------------------
print("\n--- else + finally ---")
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")     # শুধু error না হলে
finally:
    print("--- Attempt complete ---")  # সবসময়


# --------------------------------------------
# 4. raise — নিজে Error তোলা
# --------------------------------------------
print("\n--- raise ---")

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"Error: {e}")


# --------------------------------------------
# 5. Custom Exceptions
# --------------------------------------------
print("\n--- Custom Exceptions ---")

class InsufficientFundsError(Exception):
    pass

class NegativeAmountError(Exception):
    pass

def withdraw(balance, amount):
    if amount < 0:
        raise NegativeAmountError("Amount cannot be negative!")
    if amount > balance:
        raise InsufficientFundsError(f"Need {amount} but have {balance}")
    return balance - amount

try:
    result = withdraw(1000, 1500)
except InsufficientFundsError as e:
    print(f"Insufficient Funds: {e}")
except NegativeAmountError as e:
    print(f"Invalid Amount: {e}")


# --------------------------------------------
# 6. Safe Input Pattern
# --------------------------------------------
print("\n--- Safe Input Pattern ---")

def get_integer_input(prompt):
    """Valid integer না পাওয়া পর্যন্ত loop করে"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer!")

age = get_integer_input("Enter your age: ")
print(f"Your age is {age}")


# ============================================
# PRACTICE QUESTIONS
# ============================================

# --------------------------------------------
# Q1: Safe Calculator
# --------------------------------------------
print("\n--- Q1: Safe Calculator ---")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b   # ZeroDivisionError intentionally propagate করছি

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        else:
            print("Invalid operation!")
            continue

    except ValueError:
        print("Invalid input! Please enter numbers.")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print(f"Result: {result}")     # শুধু error না হলে
    finally:
        print("Calculation complete")     # সবসময়

    again = input("Calculate again? (yes/no): ")
    if again.lower() != "yes":
        break


# --------------------------------------------
# Q2: Safe Dictionary Access
# --------------------------------------------
print("\n--- Q2: Safe Dictionary Access ---")

def safe_get(dictionary, key):
    """Key না থাকলে None return করে, crash করে না"""
    try:
        return dictionary[key]
    except KeyError:
        return None

student = {
    "name": "Tariqul",
    "age": 20,
    "city": "Daqing",
    "marks": 85
}

print(safe_get(student, "name"))      # Tariqul
print(safe_get(student, "age"))       # 20
print(safe_get(student, "marks"))     # 85
print(safe_get(student, "email"))     # None
print(safe_get(student, "phone"))     # None
print(safe_get(student, "country"))   # None


# --------------------------------------------
# Q3: Age Validator with raise
# --------------------------------------------
print("\n--- Q3: Age Validator ---")

def validate_age(age):
    """Valid age না হলে ValueError raise করে"""
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age

# বিভিন্ন case test করা
test_ages = [-5, 25, 200, 0, 150]

for age in test_ages:
    try:
        valid_age = validate_age(age)
        print(f"Valid age: {valid_age}")
    except ValueError as e:
        print(f"Error for age {age}: {e}")


# --------------------------------------------
# Q4: Safe List Access
# --------------------------------------------
print("\n--- Q4: Safe List Access ---")

def safe_index(lst, index):
    """IndexError বা TypeError হলে graceful message return করে"""
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"
    except TypeError:
        return "Invalid index type"

my_list = [10, 20, 30, 40, 50]

print(safe_index(my_list, 2))      # 30 — valid
print(safe_index(my_list, 10))     # Index out of range
print(safe_index(my_list, -1))     # 50 — negative index valid
print(safe_index(my_list, "a"))    # Invalid index type


# --------------------------------------------
# Q5: Robust Number Input + BMI Calculator
# --------------------------------------------
print("\n--- Q5: BMI Calculator ---")

def get_positive_number(prompt):
    """
    User থেকে positive number নেয়।
    Invalid বা negative হলে আবার চায়।
    """
    while True:
        try:
            number = float(input(prompt))
            if number <= 0:
                raise ValueError("Number must be positive")
            return number
        except ValueError as error:
            print(f"Invalid input: {error}")

weight = get_positive_number("Enter your weight (kg): ")
height = get_positive_number("Enter your height (m): ")

bmi = weight / (height ** 2)
bmi_rounded = round(bmi, 2)

print(f"\nYour BMI is: {bmi_rounded}")

# BMI Category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")