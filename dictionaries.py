# Dictionaries
# store value in key value pair like object in js

band = {
    "vocals":"Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# access items
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# verify key exist
print("guitar" in band)
print("gui" in band)

# change values
band['vocals'] = "Cover"
band.update({"bass":"JPJ"})
print(band)

# Remove item
print(band.pop("bass"))
print(band)

print(band.popitem()) # remove last added item

# delete
band["drums"] = "bohem"
del band["drums"]
print(band)

band2.clear()
print(band2)
del band2

# copy dictionaries
# band2 = band  # create a reference
print("bad copy")

band2 = band.copy()
band2['drums'] = 'dave'
print("good copy")
print(band)
print(band2)

# use constructor
band3 = dict(band)
print(band3)

# Nested distionary
member1 = {
    "name": "palt"
}
member2 = {
    "name": "pat"
}
band = {
    "memeber1":member1,
    "memeber2":member2
}
print(band)
print(band["memeber1"]["name"])

# Sets no  duplicate allowed
nums = {1,2,3,4}

nums2 = set((1,2,3,4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# duplicates are ignored
nums3 = {1,2,3,3}
print(nums3)

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in a  set
print(2 in nums)

# but you cant refer to an element in the set with an index position or a key

# Add a new element to a set
nums.add(8)
print(nums)

# add elements from one set to another
morenums = {5,6,7}
nums.update(morenums)
print(nums)

# you cant use update with lists, tuples and dictionaries

# Merge two sets to create a new set
one = {1,2,3}
two ={4,5,6}
mynewset = one.union(two)
print(mynewset)


# keep only the duplicates
one = {1,2,3}
two ={1,3,6}

one.intersection_update(two)
print(one)

# keep everything except the duplicates
one = {1,2,3}
two ={1,3,6}

one.symmetric_difference_update(two)
print(one)