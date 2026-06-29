# ============================================
# DAY 4: Loops — for
# ============================================

# --------------------------------------------
# 1. range() — Basic Usage
# --------------------------------------------
print("--- range(5) ---")
for i in range(5):
    print(i)

print("\n--- range(2, 8) ---")
for i in range(2, 8):
    print(i)

print("\n--- range(0, 10, 2) ---")
for i in range(0, 10, 2):
    print(i)


# --------------------------------------------
# 2. Looping over a String
# --------------------------------------------
print("\n--- Loop over string ---")
name = "Python"

for letter in name:
    print(letter)

# enumerate() — index + value একসাথে
print("\n--- enumerate() ---")
for index, letter in enumerate(name):
    print(index, letter)


# --------------------------------------------
# 3. Looping over a List
# --------------------------------------------
print("\n--- Loop over list ---")
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# --------------------------------------------
# 4. Nested Loops (Pattern Printing)
# --------------------------------------------
print("\n--- Nested loop pattern ---")
for i in range(1, 4):
    for j in range(i):
        print("*", end="")
    print()


# --------------------------------------------
# 5. break and continue
# --------------------------------------------
print("\n--- break demo ---")
for i in range(10):
    if i == 5:
        break
    print(i)

print("\n--- continue demo ---")
for i in range(10):
    if i == 5:
        continue
    print(i)


# ============================================
# PRACTICE QUESTIONS
# ============================================

# --------------------------------------------
# Q1: Print 1 to 10
# --------------------------------------------
print("\n--- Q1: 1 to 10 ---")
for i in range(1, 11):
    print(i)


# --------------------------------------------
# Q2: Even numbers from 1 to 50 (using step)
# --------------------------------------------
print("\n--- Q2: Even numbers 1-50 ---")
for i in range(2, 51, 2):
    print(i)


# --------------------------------------------
# Q3: Reverse a string
# --------------------------------------------
print("\n--- Q3: Reverse String ---")
text = input("Enter a string: ")

for i in range(len(text) - 1, -1, -1):
    print(text[i])


# --------------------------------------------
# Q4: Multiplication Table (1 to 5, nested loop)
# --------------------------------------------
print("\n--- Q4: Multiplication Table ---")
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()


# --------------------------------------------
# Q5: Sum 1 to 100, break when sum exceeds 500
# --------------------------------------------
print("\n--- Q5: Sum until 500 ---")
total = 0
for i in range(1, 101):
    total += i
    if total > 500:
        print("500 ছাড়িয়েছে এই সংখ্যায়:", i)
        print("Total Sum:", total)
        break