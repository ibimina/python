# list hold multiple values

users = ["mina", "42", "sare"]
data = ["Dave", 42, True]
emptylist = []

print("Dave" in emptylist)
print(users[0])
print(users[-2])

print(users.index("sare"))
print(users[0:2])

print(users[-3:-1])
print(len(data))

users.append('hart')
print(users)

users += ['Jason']
print(users)

users.extend(['robert', 'jim'])
print(users)

# users.extend(data)
# print(users)

users.insert(0,'Bob')
print(users)

users[2:2] = ['Eddie',"Alex"]
print(users)

users[1:3] = ['grace',"Alex"]
print(users)

users.remove("Bob")

users.pop()

# delete
del users[0]
data.clear()
del data

users.sort()
users[1:2] = ['dave']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4,45,78,1,5]
nums.reverse()

print(nums)

nums.sort(reverse=True)
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(type(nums))
nums2 = list([1,1,3])
print(isinstance)