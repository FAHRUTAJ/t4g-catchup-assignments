# Task 1: Arithmetic
num1 = 10
num2 = 3
f1 = 5.5
f2 = 2.0

print(num1 + num2)  # Addition
print(num1 - num2)  # Subtraction
print(num1 * num2)  # Multiplication
print(num1 / num2)  # Division (float)
print(num1 // num2) # Floor Division (drops remainder)
print(num1 % num2)  # Modulo (returns remainder)
print(num1 ** num2) # Exponentiation (10 to the power of 3)

# Task 2: Rectangle Math
length = 15.5
width = 8
area = length * width
perimeter = 2 * (length + width)
print(f"A rectangle with length {length} and width {width} has an area of {area} and a perimeter of {perimeter}.")

# Task 3: Conversions & Type Checking
my_int = 7
my_float = float(my_int)
print(my_float)

orig_float = 9.99
new_int = int(orig_float) # Note: this truncates, it doesn't round!
print(new_int)

print(type(num1), type(f1), type(area), type(new_int))