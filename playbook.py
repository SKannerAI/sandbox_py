'''a = True
b = False

if b:
    print("a is True")
if not a:
    print("b is False")
elif a and not b:
    print("a is True and b is False")

a = [1,2,3,4,5,6]

for item in a:
    print(item)

if 5 in a:
    print("5 is in the list")'''
'''
def factorial(num):
    if (type(num) != int or num < 0):
        return None
    else:
        temp = 0
        fact = 1
        while (num >1):
            temp = num
            fact = fact * temp
            num = num - 1
        return fact
print(factorial(6))

a = [1,2,3]
b = a
a.append(5)
a = [4,5,6]


print(a)
print(b)

c=(1,2,3)
print(type(c))

d = {4,5,6}
print(type(d))

animals = {'a':'antelope', 'b':'buffalo', 'c':'cat'}

print(animals['a'])

animals['d'] = 'donkey'

print(animals)

print(set(animals.keys()))
animals.values()

# List Comprehension 
# [expression for item in iterable]
myList = list(range(10))

newlist = [2 * item for item in myList]
print(newlist)

selective_list = [item for item in myList if item%2 == 0]
print(selective_list)

# String manipulation
myString = 'My name is Sandeep Kanparthy. I am learning Python programming'

def cleanWords(word):
    return word.replace('.','').lower()
print([cleanWords(w) for w in myString.split()])

# Dictionary manipulation
animalList = [('a', 'antelope'), ('b', 'buffalo'), ('c', 'cat')]
newDictionary = {item[0]: item[1] for item in animalList}

print((newDictionary))
extendedAnimalList = [('a', 'antelope', 'fast'),
                      ('b', 'buffalo', 'slow'), ('c', 'cat', 'jumpy')]
animals = {key: value+' is '+speed for key, value, speed in extendedAnimalList}
print(animals)

my_string = "Hello my name is Sandeep"
print(my_string[::-1])

age = 22
message = "Eligible" if age > 18 else "Not Eligigle"
print(message)

if 18 <= age < 65:
    print("Hello")
else:
    print("Not right")

success = False
for number in range(3):
    print("Attempt", number+1, (number+1)*".")
    if (success):
        print("Successful")
        break
else:
    print("All attempts failed")

for x in range(3):
    for y in range(3):
        print(f"({x}, {y})")


while True:
    command = input(">>")
    if command == "quit":
        break
print(f"ECHO", command)

temp_list = []
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
        temp_list.append(i)

print(f"We have {len(temp_list)} even numbers")


def increment(x, by=1):
    return x+by


print(increment(2, 4))


def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total


print(multiply(2, 3, 4, 5))'''


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))
