#Task 1: Calculate area and perimeter of a rectangle
# Length and width of the rectangle
length = 10  # in meters
width = 5    # in meters

# Area = length × width
area = length * width

# Perimeter = 2 × (length + width)
perimeter = 2 * (length + width)

print("Area of rectangle:", area, "sq.meters")
print("Perimeter of rectangle:", perimeter, "meters")

#---------------------------------------------------------------

# Task 2: Take two numbers as input and compare them
# Input from user (convert to float for decimal support)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Compare and print result
if num1 > num2:
    print("First number is greater.")
elif num1 < num2:
    print("First number is smaller.")
else:
    print("Both numbers are equal.")

#---------------------------------------------------------------
# Task 3: Check if a given year is a leap year

year = int(input("Enter a year: "))

# A leap year is:
# divisible by 4 AND not divisible by 100
# OR divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

#---------------------------------------------------------------
# Task 4: Play with arithmetic and logical operators

a = 15
b = 4

# Arithmetic operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus (Remainder):", a % b)
print("Exponentiation:", a ** b)

# Comparison operators
print("Is a > b?", a > b)
print("Is a equal to b?", a == b)

# Logical operators
print("Logical AND (a > 10 and b < 5):", a > 10 and b < 5)
print("Logical OR (a < 10 or b < 5):", a < 10 or b < 5)
print("Logical NOT (not a > b):", not a > b)

# Assignment operators
a += 2
print("Value of a after a += 2:", a)

#---------------------------------------------------------------
# Task 5: Concatenate and print two strings

first_name = "Misha"
last_name = "Singla"

# Combine strings using +
full_name = first_name + " " + last_name

print("Full Name:", full_name)


