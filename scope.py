name = "hart" # global scope
count = 1
def another():
    color = "blue" # local scope
    print(name) # print global name
    global count
    count += 1
    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name) # print local scope

    greeting("Dave")

another()

print(name)
