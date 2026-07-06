# ============================================
# DAY 6: Strings Deep Dive
# ============================================

# --------------------------------------------
# 1. String Indexing
# --------------------------------------------
print("--- String Indexing ---")
name = "Python"
#       012345   (positive index)
#      -6-5-4-3-2-1  (negative index)

print(name[0])     # P
print(name[3])     # h
print(name[-1])    # n (শেষ character)
print(name[-2])    # o (শেষ থেকে দ্বিতীয়)


# --------------------------------------------
# 2. String Slicing
# --------------------------------------------
print("\n--- String Slicing ---")
text = "Hello, World!"

print(text[0:5])    # Hello
print(text[7:])     # World!
print(text[:5])     # Hello
print(text[-6:])    # orld!
print(text[::2])    # Hlo ol!
print(text[::-1])   # !dlroW ,olleH (reverse)


# --------------------------------------------
# 3. String Methods
# --------------------------------------------
print("\n--- upper / lower / title ---")
text = "hello world"
print(text.upper())    # HELLO WORLD
print(text.lower())    # hello world
print(text.title())    # Hello World

print("\n--- strip ---")
text = "   Hello World   "
print(text.strip())     # "Hello World"
print(text.lstrip())    # "Hello World   "
print(text.rstrip())    # "   Hello World"

print("\n--- replace ---")
text = "I love JavaScript"
print(text.replace("JavaScript", "Python"))

print("\n--- split ---")
sentence = "apple,banana,mango"
fruits = sentence.split(",")
print(fruits)    # ['apple', 'banana', 'mango']

words = "Hello World Python".split()
print(words)     # ['Hello', 'World', 'Python']

print("\n--- join ---")
fruits = ["apple", "banana", "mango"]
print(", ".join(fruits))     # apple, banana, mango
print(" | ".join(fruits))    # apple | banana | mango

print("\n--- find / in ---")
text = "Hello, Python World"
print(text.find("Python"))    # 7
print(text.find("Java"))      # -1
print("Python" in text)       # True
print("Java" in text)         # False

print("\n--- startswith / endswith ---")
email = "tariqul@gmail.com"
print(email.startswith("tariqul"))    # True
print(email.endswith(".com"))         # True
print(email.endswith(".org"))         # False

print("\n--- count / len ---")
text = "banana"
print(text.count("a"))    # 3
print(len(text))          # 6


# --------------------------------------------
# 4. String Immutability
# --------------------------------------------
print("\n--- Immutability ---")
name = "Python"
new_name = "J" + name[1:]    # slicing দিয়ে নতুন string
print(new_name)               # Jython


# --------------------------------------------
# 5. f-string Advanced
# --------------------------------------------
print("\n--- f-string Advanced ---")
name = "Tariqul"
age = 21
score = 95.5678

print(f"Name: {name}")
print(f"Age next year: {age + 1}")
print(f"Score: {score:.2f}")
print(f"Name length: {len(name)}")
print(f"Uppercase: {name.upper()}")
print(f"{'Python':>10}")     # right align
print(f"{'Python':<10}!")    # left align


# ============================================
# PRACTICE QUESTIONS
# ============================================

# --------------------------------------------
# Q1: Palindrome Checker
# --------------------------------------------
print("\n--- Q1: Palindrome Checker ---")
word = input("Enter a word: ")
word = word.lower()

if word == word[::-1]:
    print("Palindrome ✅")
else:
    print("Not Palindrome ❌")


# --------------------------------------------
# Q2: Word Counter
# --------------------------------------------
print("\n--- Q2: Word Counter ---")
sentence = input("Enter a sentence: ")
words = sentence.split()

print("Total words:", len(words))
print("Unique words:", len(set(words)))

max_char = ""
max_count = 0
for ch in sentence:
    if ch == " ":
        continue
    count = sentence.count(ch)
    if count > max_count:
        max_count = count
        max_char = ch

print("Most frequent character:", max_char)
print("Frequency:", max_count)


# --------------------------------------------
# Q3: Email Validator
# --------------------------------------------
print("\n--- Q3: Email Validator ---")
email = input("Enter your email: ")

if "@" in email and (email.endswith(".com") or email.endswith(".org")):
    print("Valid email ✅")
else:
    print("Invalid email ❌")


# --------------------------------------------
# Q4: String Formatter
# --------------------------------------------
print("\n--- Q4: String Formatter ---")
name = input("Enter your name: ")

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Title Case:", name.title())
print("With Hyphen:", "-".join(name))
print("Reverse:", name[::-1])


# --------------------------------------------
# Q5: Caesar Cipher
# --------------------------------------------
print("\n--- Q5: Caesar Cipher ---")
word = input("Enter a word: ")
shift = 3
encrypted = ""

for ch in word:
    encrypted += chr(ord(ch) + shift)

print("Encrypted:", encrypted)

# Bonus — Decrypt করাও সম্ভব:
decrypted = ""
for ch in encrypted:
    decrypted += chr(ord(ch) - shift)
print("Decrypted:", decrypted)