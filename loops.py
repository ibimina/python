value  = 1
# while loop

# while value < 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# while value < 10:
#     value += 1
#     if value == 5:
#         continue # when value is 5 no value is printed
#     print(value)
# else:
#     print(value)


# For loop
names = ["a","b","c"]
# for x in names:
#     print(x)

# for x in names:
#     if x == "b":
#         break
#     print(x)

for x in names:
    if x == "b":
        print(x)
        continue

for x in range(4):
    print(x)

for x in range(2, 4):
    print(x)   

for x in range(5, 100, 5):
     print(x)  
else:
    print("Glad that\'s over!")   

actions = ['code',"eats","sleeps"]
for name in names:
    for action in actions:
        print(name + "" + action + ".")