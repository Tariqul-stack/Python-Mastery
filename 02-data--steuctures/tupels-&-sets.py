# ============================================
# DAY 9: Tuples + Sets
# ============================================

# --------------------------------------------
# 1. Tuple — Basic Concept
# --------------------------------------------
print("--- Tuple vs List ---")
fruits_list = ["apple", "banana", "mango"]
fruits_tuple = ("apple", "banana", "mango")

# List change করা যায়
fruits_list[0] = "grape"
print("List (changed):", fruits_list)

# Tuple change করা যায় না
# fruits_tuple[0] = "grape"  # ❌ ERROR — immutable


# --------------------------------------------
# 2. Tuple Operations
# --------------------------------------------
print("\n--- Tuple Operations ---")
point = (10, 20, 30, 20, 10)

print(point[0])           # 10
print(point[-1])          # 10
print(point[1:3])         # (20, 30)
print(len(point))         # 5
print(point.count(10))    # 2
print(point.index(30))    # 2
print(20 in point)        # True


# --------------------------------------------
# 3. Tuple Unpacking
# --------------------------------------------
print("\n--- Tuple Unpacking ---")
point = (10, 20)
x, y = point
print(f"x = {x}, y = {y}")

# Function থেকে multiple return
def get_user():
    return ("Tariqul", 21, "BD")

name, age, country = get_user()
print(f"Name: {name}, Age: {age}, Country: {country}")

# One-liner swap
a = 10
b = 20
print(f"Before: a={a}, b={b}")
a, b = b, a
print(f"After:  a={a}, b={b}")


# --------------------------------------------
# 4. Set — Basic Concept
# --------------------------------------------
print("\n--- Set (duplicates removed) ---")
fruits = {"apple", "banana", "mango", "apple", "banana"}
print(fruits)   # duplicate বাদ হয়ে যায়


# --------------------------------------------
# 5. Set Operations
# --------------------------------------------
print("\n--- Set Operations ---")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (a-b):", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)


# --------------------------------------------
# 6. Set Methods
# --------------------------------------------
print("\n--- Set Methods ---")
fruits = {"apple", "banana", "mango"}

fruits.add("grape")
print("After add:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

fruits.discard("watermelon")   # না থাকলেও error নেই
print("After discard:", fruits)

print("Length:", len(fruits))
print("'apple' in fruits:", "apple" in fruits)


# ============================================
# PRACTICE QUESTIONS
# ============================================

# --------------------------------------------
# Q1: Tuple basics + convert to list + back
# --------------------------------------------
print("\n--- Q1: Tuple Basics ---")
person = ("Tariqul", 23, "Dhaka")

# Unpacking
name, age, city = person
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")

# Tuple → List → add → Tuple
person_list = list(person)
person_list.append("Beijing")
updated_person = tuple(person_list)
print("Updated Tuple:", updated_person)


# --------------------------------------------
# Q2: One-liner swap
# --------------------------------------------
print("\n--- Q2: Swap ---")
a = "Hello"
b = "World"

print("Before Swap:")
print("a =", a)
print("b =", b)

a, b = b, a   # one-liner swap (tuple unpacking!)

print("\nAfter Swap:")
print("a =", a)
print("b =", b)


# --------------------------------------------
# Q3: Remove duplicates using Set
# --------------------------------------------
print("\n--- Q3: Remove Duplicates ---")
numbers = [1, 2, 3, 2, 4, 3, 5, 1, 6, 5]
unique_numbers = sorted(set(numbers))   # এক লাইনেই!
print("Unique Sorted List:", unique_numbers)


# --------------------------------------------
# Q4: Set Operations (students)
# --------------------------------------------
print("\n--- Q4: Set Operations ---")
class_a = {"Rahim", "Karim", "Jamal", "Ritu", "Sohel"}
class_b = {"Jamal", "Ritu", "Nadia", "Pavel", "Sohel"}

print("All Students (Union):")
print(class_a | class_b)

print("\nCommon Students (Intersection):")
print(class_a & class_b)

print("\nOnly in Class A (Difference):")
print(class_a - class_b)


# --------------------------------------------
# Q5: Tuple + Loop + List Comprehension
# --------------------------------------------
print("\n--- Q5: Student Marks ---")
students = [
    ("Rahim", 85),
    ("Karim", 92),
    ("Jamal", 78),
    ("Ritu", 96)
]

# সব student print
print("Student Marks:")
for name, marks in students:    # tuple unpacking in loop!
    print(f"  {name} scored {marks}")

# Highest marks (loop দিয়ে, max() ছাড়া)
top_name = ""
top_marks = 0
for name, marks in students:
    if marks > top_marks:
        top_marks = marks
        top_name = name
print(f"\nTop Student: {top_name} ({top_marks})")

# 80 এর উপরে (list comprehension + tuple unpacking)
good_students = [
    (name, marks)
    for name, marks in students
    if marks > 80
]
print("\nStudents above 80:")
for name, marks in good_students:
    print(f"  {name}: {marks}")