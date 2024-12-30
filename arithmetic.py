# python operators: symbols used to perform operations on values and variable that hold those values

# Examples
#  assigment operator =
name = "Dave"
print(name)

# arithmetic operator
num1 = 2
num2 = 24
num3 = 5

# addition
print(num1 + num1)  # 4

# substraction
print(4 - num1)  # 2
# multiply
print(num1 * num1)  # 4
# division
print(num2 / num3)  # 4.8
# round number down
print(num2 // num3)  # 4 round down

# round number up to nearest whole number
print(round(num2 / num3))  # 5 round up
# remainder 
print(num2 % num3)  # 4
# exponential
print(num1 ** 3)  # 8

print("mina " + "Gray"
)

# Comparism Operator

print(42 == 41)

print(42 == 42)

print(42 != 42)

print(43 != 42)

print(10 > 5)

print(10 < 5)

print(10 >= 10)

print(10 <= 10)

x = True
y = False
z = True

# not prints the opposite of a boolean value

print(not x)
print(not y)

# and 
# looks at two conditions e.g x and y it only looks at the second value if the first value is true
# it needs both value to be True
print(x and y) # False

print(x and y) # False

# or
# looks at two conditions e.g x or y it only looks at the second value if the first value is false
# it needs one value to be True

print(x or y) # True

print(y or x) # True

# Conditional Statement and Comparism operator
meaning = 42

if meaning > 10:
    print("Right on!")
else:
    print("Not today")

# Ternary Operator
print("Right on!") if meaning > 10 else print("Not today")