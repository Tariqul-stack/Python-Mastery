# ============================================
# DAY 12: Functions — Advanced
# ============================================

# --------------------------------------------
# 1. *args
# --------------------------------------------
print("--- *args ---")

def add(*args):
    print(f"args tuple: {args}")
    total = 0
    for num in args:
        total += num
    return total

print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 2, 3, 4, 5))


# --------------------------------------------
# 2. **kwargs
# --------------------------------------------
print("\n--- **kwargs ---")

def student_info(**kwargs):
    print(f"kwargs dict: {kwargs}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_info(name="Tariqul", age=21, city="Dhaka")


# --------------------------------------------
# 3. *args + **kwargs একসাথে
# --------------------------------------------
print("\n--- *args + **kwargs ---")

def mixed(name, *args, **kwargs):
    print(f"Name: {name}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

mixed("Tariqul", 1, 2, 3, city="Dhaka", age=21)


# --------------------------------------------
# 4. Scope — Local vs Global
# --------------------------------------------
print("\n--- Scope ---")

x = 10

def show():
    x = 20        # local variable
    print(x)      # 20

show()
print(x)          # 10 — global অপরিবর্তিত


# global keyword
print("\n--- global keyword ---")
count = 0

def increment():
    global count
    count += 1

increment()
increment()
print(count)   # 2


# --------------------------------------------
# 5. Nested Functions + Closure
# --------------------------------------------
print("\n--- Closure + Counter ---")

def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

my_counter = make_counter()
print(my_counter())   # 1
print(my_counter())   # 2
print(my_counter())   # 3


# --------------------------------------------
# 6. Lambda
# --------------------------------------------
print("\n--- Lambda ---")

square = lambda n: n ** 2
print(square(5))     # 25

students = [("Rahim", 85), ("Karim", 92), ("Jamal", 78)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

sorted_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_desc)


# map() + filter() + lambda
print("\n--- map + filter ---")
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, numbers))
print("Squared:", squared)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)


# --------------------------------------------
# 7. Higher-Order Functions
# --------------------------------------------
print("\n--- Higher-Order Functions ---")

def apply(func, value):
    return func(value)

def double(n):
    return n * 2

def triple(n):
    return n * 3

print(apply(double, 5))
print(apply(triple, 5))
print(apply(lambda x: x**2, 5))


# ============================================
# PRACTICE QUESTIONS
# ============================================

# --------------------------------------------
# Q1: multiply_all(*args) + stats(*args)
# --------------------------------------------
print("\n--- Q1: *args Functions ---")

def multiply_all(*args):
    result = 1           # 0 দিলে সব গুণ করে 0 হতো!
    for number in args:
        result *= number
    return result

def stats(*args):
    minimum = min(args)
    maximum = max(args)
    average = sum(args) / len(args)
    return minimum, maximum, average

print(multiply_all(2, 3, 4))           # 24
print(multiply_all(1, 2, 3, 4, 5))    # 120

minimum, maximum, average = stats(10, 20, 30, 40, 50)
print(f"Min: {minimum}, Max: {maximum}, Average: {average}")


# --------------------------------------------
# Q2: create_profile(**kwargs)
# --------------------------------------------
print("\n--- Q2: **kwargs Profile ---")

def create_profile(**kwargs):
    print("----- Profile -----")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print()

create_profile(
    name="Tariqul",
    age=20,
    city="Daqing"
)

create_profile(
    name="Rahim",
    job="Software Engineer",
    skills=["Python", "JavaScript", "React"],
    country="Bangladesh"
)


# --------------------------------------------
# Q3: Scope Practice
# --------------------------------------------
print("\n--- Q3: Scope ---")

x = "global"

def outer():
    x = "outer"
    def inner():
        x = "inner"
        print(x)      # inner
    inner()
    print(x)          # outer

outer()
print(x)              # global


# nonlocal দিয়ে outer এর x modify
print("\n--- nonlocal ---")

def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "modified outer"
    inner()
    print(x)          # modified outer

outer()


# --------------------------------------------
# Q4: Lambda + sorted + filter
# --------------------------------------------
print("\n--- Q4: Lambda + sorted + filter ---")

products = [
    {"name": "Laptop", "price": 999, "rating": 4.5},
    {"name": "Phone",  "price": 699, "rating": 4.8},
    {"name": "Tablet", "price": 499, "rating": 4.2},
    {"name": "Watch",  "price": 299, "rating": 4.6},
]

# Price ascending
sorted_by_price = sorted(
    products,
    key=lambda product: product["price"]
)
print("By Price (asc):")
for p in sorted_by_price:
    print(f"  {p['name']}: ${p['price']}")

# Rating descending
sorted_by_rating = sorted(
    products,
    key=lambda product: product["rating"],
    reverse=True
)
print("\nBy Rating (desc):")
for p in sorted_by_rating:
    print(f"  {p['name']}: {p['rating']}⭐")

# Price below 500
cheap_products = list(filter(
    lambda product: product["price"] < 500,
    products
))
print("\nUnder $500:")
for p in cheap_products:
    print(f"  {p['name']}: ${p['price']}")


# --------------------------------------------
# Q5: Closure — make_multiplier
# --------------------------------------------
print("\n--- Q5: Closure ---")

def make_multiplier(n):
    def multiplier(number):
        return number * n    # n টা outer scope থেকে "remember" করছে
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))              # 10
print(triple(5))              # 15
print(double(triple(4)))      # double(12) = 24 — function composition!