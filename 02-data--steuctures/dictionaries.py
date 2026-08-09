# ============================================
# DAY 10: Dictionaries
# ============================================

# --------------------------------------------
# 1. Dictionary তৈরি করা
# --------------------------------------------
print("--- Dictionary Creation ---")
person = {
    "name": "Tariqul",
    "age": 21,
    "city": "Dhaka",
    "is_student": True
}
print(person)

# Mixed types
mixed = {
    1: "one",
    "two": 2,
    "list": [1, 2, 3]
}
print(mixed)


# --------------------------------------------
# 2. Value Access করা
# --------------------------------------------
print("\n--- Accessing Values ---")
person = {"name": "Tariqul", "age": 21, "city": "Dhaka"}

# Direct access
print(person["name"])     # Tariqul

# get() — safe way
print(person.get("name"))               # Tariqul
print(person.get("email"))              # None
print(person.get("email", "Not found")) # Default value


# --------------------------------------------
# 3. Add, Update, Delete
# --------------------------------------------
print("\n--- Add / Update / Delete ---")
person = {"name": "Tariqul", "age": 21}

# Add
person["city"] = "Dhaka"
print("After add:", person)

# Update
person["age"] = 22
print("After update:", person)

# Delete
del person["city"]
print("After del:", person)

# pop()
removed = person.pop("age")
print("Popped value:", removed)
print("After pop:", person)


# --------------------------------------------
# 4. Dictionary Methods
# --------------------------------------------
print("\n--- Dictionary Methods ---")
person = {"name": "Tariqul", "age": 21, "city": "Dhaka"}

print(person.keys())      # সব keys
print(person.values())    # সব values
print(person.items())     # key-value pairs

print("name" in person)   # True
print("email" in person)  # False
print(len(person))        # 3

person.update({"email": "t@gmail.com", "age": 25})
print("After update():", person)


# --------------------------------------------
# 5. Dictionary দিয়ে Loop
# --------------------------------------------
print("\n--- Looping Dictionary ---")
person = {"name": "Tariqul", "age": 21, "city": "Dhaka"}

# শুধু keys
for key in person:
    print(key)

# শুধু values
print()
for value in person.values():
    print(value)

# key + value একসাথে
print()
for key, value in person.items():
    print(f"{key}: {value}")


# --------------------------------------------
# 6. Nested Dictionary
# --------------------------------------------
print("\n--- Nested Dictionary ---")
students = {
    "Rahim": {"age": 20, "marks": 85, "city": "Dhaka"},
    "Karim": {"age": 22, "marks": 92, "city": "Chittagong"}
}

print(students["Rahim"]["marks"])    # 85
print(students["Karim"]["city"])     # Chittagong

for name, info in students.items():
    print(f"\n{name}:")
    for key, value in info.items():
        print(f"  {key}: {value}")


# --------------------------------------------
# 7. Dictionary Comprehension
# --------------------------------------------
print("\n--- Dictionary Comprehension ---")
numbers = [1, 2, 3, 4, 5]

squares = {n: n**2 for n in numbers}
print("Squares:", squares)

even_squares = {n: n**2 for n in numbers if n % 2 == 0}
print("Even Squares:", even_squares)


# ============================================
# PRACTICE QUESTIONS
# ============================================

# --------------------------------------------
# Q1: Student Info System
# --------------------------------------------
print("\n--- Q1: Student Info System ---")
student = {
    "name": "Tariqul Islam",
    "age": 20,
    "city": "Daqing",
    "marks": 85,
    "hobby": "Swimming"
}

print("Keys:", student.keys())
print("Values:", student.values())
print("Email:", student.get("email", "Email not found"))

student["marks"] = 90
print("Updated marks:", student)

del student["hobby"]
print("After deleting hobby:", student)


# --------------------------------------------
# Q2: Word Frequency Counter
# --------------------------------------------
print("\n--- Q2: Word Frequency Counter ---")
sentence = "the cat sat on the mat the cat"
words = sentence.split()

frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1    # আগে দেখেছি — count বাড়াও
    else:
        frequency[word] = 1     # প্রথমবার দেখছি — 1 দিয়ে শুরু

for word, count in frequency.items():
    print(f"{word}: {count}")


# --------------------------------------------
# Q3: Nested Dictionary + Highest Marks
# --------------------------------------------
print("\n--- Q3: Nested Student Dictionary ---")
students = {
    "student1": {"name": "Rahim", "age": 20, "marks": 85},
    "student2": {"name": "Karim", "age": 21, "marks": 92},
    "student3": {"name": "Hasan", "age": 19, "marks": 78}
}

# সবার নাম এবং marks
for student in students.values():
    print(f"{student['name']}: {student['marks']}")

# Highest marks
highest_student = None
highest_marks = 0
for student in students.values():
    if student["marks"] > highest_marks:
        highest_marks = student["marks"]
        highest_student = student["name"]

print(f"\nHighest Marks: {highest_student} ({highest_marks})")


# --------------------------------------------
# Q4: Dictionary Comprehension
# --------------------------------------------
print("\n--- Q4: Word Length Dictionary ---")
words = ["python", "java", "javascript", "rust", "go"]

word_length = {word: len(word) for word in words}
print(word_length)


# --------------------------------------------
# Q5: Phone Book App
# --------------------------------------------
print("\n--- Q5: Phone Book ---")
phone_book = {
    "Rahim": "01711111111",
    "Karim": "01822222222",
    "Hasan": "01933333333",
    "Sakib": "01644444444",
    "Nabil": "01555555555"
}

while True:
    print("\n1. Search Contact")
    print("2. Add Contact")
    print("3. Show All Contacts")
    print("4. Exit")
    choice = input("Choose option: ")

    if choice == "1":
        name = input("Enter name: ")
        number = phone_book.get(name, "Contact not found")
        print(number)

    elif choice == "2":
        name = input("Enter new name: ")
        number = input("Enter phone number: ")
        phone_book[name] = number
        print("Contact added successfully!")

    elif choice == "3":
        print("\nAll Contacts (Alphabetical):")
        for name in sorted(phone_book):
            print(f"  {name}: {phone_book[name]}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option! Please choose 1-4.")