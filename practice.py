#Q1
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")

#Q2
gender = input("Enter your gender (M/F): ")
if gender == "M" or gender == "m":
    print("Good morning sir")
elif gender == "F" or gender == "f":
    print("Good morning mam")
else:
    print("Please enter a valid gender (M/F)")

Create a table using for loop
n = int(input("Which table number do you want? "))

for i in range(n,(n*10)+1,n):
    print (i)

# Print perfect number
n = int(input("Check your number is perfect or not: "))

sum = 0 
for i in range(1,n):
    if n%i == 0:
        sum = sum + i
if sum == n:
    print("Your Number is perfect")
else:
    print("Your number is not perfect")       

#  Find Prime Number
n = int(input("Check your number is prime or not: "))   
count = 0
for i in range(1,n+1):
    if n%i ==0:
        count = count + 1
if count == 2:
    print("your number is prime")
else:
    print("Your number is not prime")   
