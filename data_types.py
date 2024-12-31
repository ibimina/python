import math

# String

# Literal assignment
first = "mina"
last = "Hart"

# type of value
print(type(first))
print(type(first) == str)
print(isinstance(first,str))

# constructor function
rice = str("Jollof")

print(type(rice))
print(type(rice) == str)
print(isinstance(rice,str))

# Concatenation

fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like watching horror movies from the " + decade + "s."
print(statement)

# Multiple lines
multiline = """
Hey, how are you

I was just checking in.
                    All good?
"""
print(multiline)

# Escaping special charcaters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String methods
print(first)
print(first.lower())
print(first.upper())
print(first.capitalize())

print(multiline.title())
print(multiline.replace("good", 'ok'))

print(len(multiline)) # length of a string

print(multiline.strip()) # removes white space

print(multiline.lstrip()) # removes white space from the left side
print(multiline.rstrip()) # removes white space from the rigth side

# Build a menu
title = "menu".upper()
print(title.center(20,"="))
print("Coffe".ljust(16,'.') + "$1".rjust(4)) 
print("Muffin".ljust(16,'.') + "$2".rjust(4)) 
print("Cheesecake".ljust(16,'.') + "$4".rjust(4)) 

# string index values
print(first[0])
print(first[-1]) # returns the last value
print(first[1:-1]) # the last range value will not be added to the range
print(first[1:])  # the range value will include the last value

# method tha return boolean value
print(first.startswith('o'))
print(first.endswith('o'))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data type
# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

#float type
gpa = 3.28
y = float(1.4)
print(type(gpa))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Builtin functions for numbers

print(abs(gpa))
print(round(gpa)) # round down to the nearest integer
print(round(gpa, 1)) # round to one decimal place


print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting string to  anumber
zipcode = '10001'
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
# zip_value = int('New york')