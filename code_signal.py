import math
from typing import List
'''
# print the century from the year provided

def calculate_century(year: int):
    return math.ceil(year/100)

year_input = input("Enter the year >> ")

century = int(year_input)

print(f"its {calculate_century(century)} Century")
'''

'''
def checkPalindrome(inputstring):
    i = 0
    j = len(inputstring) - 1
    while i < j:
        if inputstring[i] != inputstring[j]:
            return False
        i += 1
        j -= 1  # goes to next While() loop iteration
    return True  # executed after exiting While() loop


print(checkPalindrome("aa2aa"))

# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product

def adjacentElementsProduct(inputArray: List[int]):
    return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])


print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))

# Arrange statues from smallest to largest and find out how many are missing in between to complete the sequence


def makeArrayConsecutive2(statues):
    additionalStatuesCounter = 0
    statues.sort()
    print(f"Sorted Statues = {statues}")

    for i in range(0, len(statues)-1):
        if (statues[i+1] - statues[i] > 1):
            additionalStatuesCounter += statues[i+1] - statues[i] - 1

    return additionalStatuesCounter


statues = [6, 2, 3, 8]

print(makeArrayConsecutive2(statues))

# If Zero represents an empty room in a hotel, return the sum of all non-zero room numbers which do not have an empty room(zero) below it
matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]


def matrixElementsSum(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    cols = []
    for c in range(columns):
        col = []
        for r in range(rows):
            col.append(matrix[r][c])
        cols.append(col)
    print(cols)

    sum = 0
    for arr in cols:
        for n in arr:
            if n == 0:
                break
            sum += n
    return sum 
# alternate execution
matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]


def matrixElementsSum(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    sum = 0
    for c in range(columns):
        for r in range(rows):
            if matrix[r][c] == 0:
                break
            sum += matrix[r][c]

    return sum


print(matrixElementsSum(matrix))

def allLongestString(inputArray):
    m = len(max(inputArray, key=len))
    return [item for item in inputArray if len(item) == m]


print(allLongestString(["aaa", "ab", "vf", "abh", "yht"]))'''
