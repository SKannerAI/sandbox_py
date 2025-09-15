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

print(makeArrayConsecutive2(statues))'''
