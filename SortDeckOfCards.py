def solution(deck):

    # Start from the end and find the longest suffix that's already sorted
    i = len(deck) - 1

    # Move backwards while cards are in correct ascending order
    while i > 0 and deck[i-1] < deck[i]:
        i -= 1

    # Take elements from index 3 to end, then elements from start to index 3
    new_deck = deck[i:] + deck[:i]
    print(new_deck)

    if sorted(deck) != new_deck:
        return -1
    # The number of shuffle moves needed is the number of cards before the sorted suffix
    return i


testDeck = [3, 4, 5, 1, 2]
testDeck2 = [4, 5, 1, 2, 3]
testDeck3 = [4, 1, 2, 5, 3]

print(solution(testDeck))
print(solution(testDeck2))
print(solution(testDeck3))
