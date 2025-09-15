# if -1 represents a real tree and the numbers are height of people standing in a line, then sort them in ASC keeping the positions
# of the tree unchanged
def sortByHeight(a):
    holder = sorted([item for item in a if item != -1])
    j = 0
    for i in range(len(a)):
        if (a[i]) != -1:
            a[i] = holder[j]
            j += 1
    return a


print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))
