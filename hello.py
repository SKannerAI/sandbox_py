from typing import List

# Print "hello, world!" to the terminal
print('Hello, World!')


def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("Recursion Example Results:")
tri_recursion(6)

a = [1, 2, 3, 4, 5, 6]

# Dictionary
animals = {'a': 'antelope', 'b': 'buffalo', 'c': 'cat'}
print(animals['a'])
# print(type(animals))

myList = list(range(10))

newlist = [item * 2 for item in myList]
print((newlist))

filteredList = [item for item in myList if item < 8]
print(filteredList)

intro = "Hi, My name is Sandeep Kanparthy. I am looking for Engineering Manager roles in Your company"


def clean_words(sentence):
    return sentence.replace('.', '').lower()


print([clean_words(word) for word in intro.split()])

print([clean_words(word) for word in intro.split() if len(word) > 3])

print([clean_words(word) for word in intro.split()])

animalList = [('a', 'antelope'), ('b', 'buffalo'), ('c', 'cat')]

animals = {item[0]: item[1] for item in animalList}
print(animals)

animal_kv = {key: value for key, value in animalList}
print(animal_kv)


def encodeString(word):
    encoded = []
    previousChar = word[0]
    count = 1
    for currentChar in word[1:]:
        if currentChar == previousChar:
            count += 1
        else:
            encoded.append((previousChar, count))
            previousChar = currentChar
            count = 1
    encoded.append((previousChar, count))
    print(encoded)


encodeString('AAAAABBBBBCCCCCDDD')

data = [
    {'letter': 'A', 'name': 5},
    {'letter': 'B', 'name': 5},
    {'letter': 'C', 'name': 5},
    {'letter': 'D', 'name': 3}
]

result = {}
for items in data:
    key = items['name']
    # result.setdefault(key, []).append(items['letter'])
    result.setdefault(items['name'], []).append(items['letter'])
print(result)


# input list
colorsList = [2, 0, 2, 1, 1, 0]


def sort_colors(num: List[int]):
    colors = [0, 0, 0]

    for color in num:
        colors[color] += 1
    R, W, B = colors
    num[:R] = [0]*R
    num[R:R+W] = [1]*W
    num[R+W:] = [2]*B
    return num


print(sort_colors(colorsList))


def buildMatrix(rows, columns):
    ''' cols = [0]
     matrix = []
     for i in range(columns):
         cols.append(0)
     for j in range(rows):
         matrix.append(cols)'''
    # Create a matrix with all zeros
    matrix = []
    for i in range(rows):
        # Create a new row for each iteration
        row = [0] * columns
        matrix.append(row)
    return matrix


print(buildMatrix(2, 3))
