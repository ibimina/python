# single expression that returns a value
# anonymous function

squared = lambda num : num * num

print(squared(2))

addTwo = lambda num: num + 2

print(addTwo(6))

sum_total = lambda a , b: a + b

print(sum_total(3,4))

# 
def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(8))
print(addTwenty(8))

lambda num : num * num

numbers =[7,0,8,2,90]
squared_nums = map(lambda num : num * num, numbers)
print(list(squared_nums))

odd_nums = filter(lambda num : num % 2 !=0, numbers)
print(list(odd_nums))


from functools import reduce

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)
print(sum(numbers, 10))


names = ["a","b","mkk","poj"]

char_count = reduce(lambda acc, curr :acc + len(curr)
, names, 0)

print(char_count)