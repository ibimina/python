def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
      return
    return num1 + num2

total = sum(2,4)
print(total)


#  receving unknown number/multi argument

def multiple_items(*args):
   print(args)
   print(type(args))


multiple_items("Dave0","John")


def multiple_name(**args):
   print(args)
   print(type(args))


multiple_name(first="Dave0",last="John")