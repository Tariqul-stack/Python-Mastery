# ============================================
# DAY 8: Lists
# ============================================

# --------------------------------------------
# 1. List Creation + Indexing
# --------------------------------------------
print("--- List Indexing ---")
fruits = ["apple", "banana", "mango", "grape", "orange"]
#           0         1         2        3         4
#          -5        -4        -3       -2        -1

print(fruits[0])       # apple
print(fruits[-1])      # orange
print(fruits[1:3])     # ['banana', 'mango']
print(fruits[:2])      # ['apple', 'banana']
print(fruits[::2])     # ['apple', 'mango', 'orange']
print(fruits[::-1])    # reverse


# --------------------------------------------
# 2. List Methods
# --------------------------------------------
print("\n--- append / insert ---")
fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)            # ['apple', 'banana', 'mango']

fruits.insert(1, "grape")
print(fruits)            # ['apple', 'grape', 'banana', 'mango']

print("\n--- remove / pop ---")
fruits.remove("banana")
print(fruits)            # ['apple', 'grape', 'mango']

last = fruits.pop()
print("Popped:", last)   # mango
print(fruits)            # ['apple', 'grape']

print("\n--- sort / reverse ---")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers)           # ascending

numbers.sort(reverse=True)
print(numbers)           # descending

fruits = ["banana", "apple", "mango"]
fruits.reverse()
print(fruits)            # ['mango', 'apple', 'banana']

print("\n--- len / count / index ---")
nums = [1, 2, 3, 2, 2, 4]
print(len(nums))         # 6
print(nums.count(2))     # 3
print(nums.index(3))     # 2

print("\n--- in operator ---")
fruits = ["apple", "banana", "mango"]
print("apple" in fruits)    # True
print("grape" in fruits)    # False


# --------------------------------------------
# 3. Loop over List
# --------------------------------------------
print("\n--- Loop over list ---")
for fruit in fruits:
    print(fruit)

print("\n--- enumerate ---")
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")


# --------------------------------------------
# 4. List Comprehension
# --------------------------------------------
print("\n--- List Comprehension ---")
numbers = [1, 2, 3, 4, 5]

doubled = [n * 2 for n in numbers]
print("Doubled:", doubled)      # [2, 4, 6, 8, 10]

evens = [n for n in numbers if n % 2 == 0]
print("Evens:", evens)          # [2, 4]

squares = [n ** 2 for n in numbers]
print("Squares:", squares)      # [1, 4, 9, 16, 25]


# ============================================
# PRACTICE QUESTIONS
# ============================================

# --------------------------------------------
# Q1: Sum, Largest, Reverse (manually)
# --------------------------------------------
print("\n--- Q1: Sum, Largest, Reverse ---")
numbers = [10, 25, 7, 40, 15]

# Sum
total = 0
for num in numbers:
    total += num
print("Total =", total)

# Largest
largest = numbers[0]    # 0 দিয়ে শুরু না করে প্রথম element দিয়ে শুরু
for num in numbers:
    if num > largest:
        largest = num
print("Largest =", largest)

# Reverse (slicing)
print("Reverse =", numbers[::-1])


# --------------------------------------------
# Q2: User Input + sort + list comprehension
# --------------------------------------------
print("\n--- Q2: Input List ---")
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("Original List =", numbers)
print("Sorted List =", sorted(numbers))    # নতুন sorted list return করে

even_numbers = [num for num in numbers if num % 2 == 0]
print("Even Numbers =", even_numbers)


# --------------------------------------------
# Q3: Count duplicates + unique list
# --------------------------------------------
print("\n--- Q3: Duplicates ---")
numbers = [1, 2, 2, 3, 3, 3, 4]

print("Count of each unique number:")
for num in set(numbers):    # set() দিয়ে unique values
    print(f"  {num} appears {numbers.count(num)} times")

unique_numbers = list(set(numbers))
print("Unique List =", unique_numbers)


# --------------------------------------------
# Q4: Merge lists + squares
# --------------------------------------------
print("\n--- Q4: Merge + Squares ---")
list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged = list1 + list2
print("Merged List =", merged)

squares = [num ** 2 for num in merged]
print("Squares =", squares)


# --------------------------------------------
# Q5: Filter, uppercase, sort (list comprehension)
# --------------------------------------------
print("\n--- Q5: Names List ---")
names = ["Rahim", "Karim", "Alex", "Jennifer", "Tariqul", "Tom"]

long_names = [name for name in names if len(name) > 5]
print("Names longer than 5 letters =", long_names)

upper_names = [name.upper() for name in names]
print("Uppercase =", upper_names)

sorted_names = sorted(names)
print("Sorted =", sorted_names)