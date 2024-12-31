# Tuple can not be change
mytuple = tuple(("Bae", 1, True))

another = tuple((1,2,3,3,5))

print(mytuple)
print(another)

# Updating a tuple
newlist = list(mytuple)
newlist.append("Neil")
newtuple = tuple(newlist)
print(newtuple)

# destructing a tuple
(one, two, *hey) = another

print(one)
print(two)
print(hey)

print(mytuple.count(2))



