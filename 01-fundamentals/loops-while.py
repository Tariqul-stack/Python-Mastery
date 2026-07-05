# ============================================
# DAY 5: Loops — while
# ============================================

# --------------------------------------------
# 1. Basic while loop
# --------------------------------------------
print("--- Basic while loop ---")
i = 0
while i < 5:
    print(i)
    i += 1


# --------------------------------------------
# 2. while loop with user input
# --------------------------------------------
print("\n--- while with user input ---")
user_input = ""
while user_input != "quit":
    user_input = input("Type something (or 'quit' to exit): ")
    print(f"You typed: {user_input}")
print("Loop ended!")


# --------------------------------------------
# 3. while True with break
# --------------------------------------------
print("\n--- while True + break ---")
while True:
    answer = input("Enter 'yes' to continue: ")
    if answer == "yes":
        print("Continuing...")
    else:
        print("Exiting...")
        break


# --------------------------------------------
# 4. break and continue in while
# --------------------------------------------
print("\n--- break demo ---")
i = 0
while i < 10:
    if i == 6:
        break
    print(i)
    i += 1

print("\n--- continue demo ---")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


# ============================================
# PRACTICE QUESTIONS
# ============================================

# --------------------------------------------
# Q1: Countdown Timer
# --------------------------------------------
print("\n--- Q1: Countdown Timer ---")
num = int(input("Enter a number: "))
while num >= 0:
    print(num)
    num -= 1
print("Blast off! 🚀")


# --------------------------------------------
# Q2: Sum of Digits
# --------------------------------------------
print("\n--- Q2: Sum of Digits ---")
num = int(input("Enter a positive number: "))
total = 0
while num > 0:
    digit = num % 10   # last digit বের করো
    total += digit     # total এ যোগ করো
    num //= 10         # last digit বাদ দাও
print("Sum of digits =", total)


# --------------------------------------------
# Q3: Password Validator (max 3 attempts)
# --------------------------------------------
print("\n--- Q3: Password Validator ---")
correct_password = "python123"
attempts = 0

while attempts < 3:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted!")
        break
    else:
        attempts += 1
        print("Wrong password, try again")

if attempts == 3:
    print("Account locked!")


# --------------------------------------------
# Q4: Number Guessing Game (max 7 attempts)
# --------------------------------------------
print("\n--- Q4: Number Guessing Game ---")
secret = 25
attempts = 0
max_attempts = 7

while attempts < max_attempts:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1

    if guess == secret:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")

if attempts == max_attempts and guess != secret:
    print("Game over!")
    print("The number was", secret)


# --------------------------------------------
# Q5: Multiplication Table (while loop)
# --------------------------------------------
print("\n--- Q5: Multiplication Table ---")
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1