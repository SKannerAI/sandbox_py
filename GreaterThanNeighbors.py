# Find all elements in an array that are greater than both neighbors
def solution(target):
    if len(target) <= 2:
        return target

    result = []
    # Always append the first element
    result.append(target[0])

    for i in range(1, len(target)-1):
        if target[i-1] < target[i] > target[i+1]:
            result.append(target[i])
    # Add the final element since it has only one neighbor
    result.append(target[i+1])
    return result


input_array = [1, 2, 1, 4, 2]
print(solution(input_array))
