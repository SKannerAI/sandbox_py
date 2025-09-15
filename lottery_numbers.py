# a lottery number is considered Lucky if the sum of first half of the number is equal to the sum of the second half of the number


def isLucky(n):
    s = str(n)
    first_half = sum([int(x) for x in s[0:int(len(s)/2)]])
    second_half = sum(int(x) for x in s[int(len(s)/2):len(s)])
    print(first_half, second_half)
    return first_half == second_half


print(f"Is this number lucky ?? {isLucky(1230)}")
