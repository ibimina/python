person = "Dave"
coins = 3

message = "\n" + person + "has" + str(coins)
print(message)

message = "\n%s has %s coins left" % (person, coins)
print(message)

# new method
message = "\n {} has {} coins left".format(person, coins)
print(message)

message = "\n {0} has {1} coins left".format(person, coins)
print(message)

message = "\n {person} has {coins} coins left".format(person=person, coins=coins)
print(message)


player = {"person":"Dave", "coins":3}
message = "\n {person} has {coins} coins left".format(**player)
print(message)


# f-Strings
message = f"\n{person} has {coins} coins left"
print(message)
