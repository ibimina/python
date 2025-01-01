value = True

while value:
    print(value)
    value = False

value = "y"

while value:
    print(value)
    value = 0

count = 0
value1 = "x"
while value1:
    count += 1
    print(count)
    if count == 5:
        break
    else:
      value1 = 0
      continue