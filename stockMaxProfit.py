'''def maxProfit(prices):
    """
    Find maximum profit from buying and selling stock.
    Can hold at most one share at any time, but can buy and sell on same day.

    Args:
        prices: List of integers representing stock prices on each day

    Returns:
        Maximum profit achievable
    """
    if len(prices) <= 1:
        return 0

    total_profit = 0

    # Capture every profitable opportunity
    for i in range(1, len(prices)):
        # If price increased from previous day, add the difference to profit
        if prices[i] > prices[i-1]:
            total_profit += prices[i] - prices[i-1]
    return total_profit'''


def maxProfit(prices):
    # Handle edge case where we can't make any trades
    if len(prices) <= 1:
        # Return 0 if array is empty or has only one element
        return 0

    # Initialize minimum price to first price
    min_price = prices[0]
    # Initialize maximum profit to 0
    max_profit = 0

    # Iterate through prices starting from second day
    for i in range(1, len(prices)):
        # Update minimum price if current price is lower
        if prices[i] < min_price:
            # Set new minimum price
            min_price = prices[i]
        else:
            # Calculate profit if we sell today
            current_profit = prices[i] - min_price
            # Update maximum profit if current profit is better
            max_profit = max(max_profit, current_profit)

    # Return the maximum profit achievable
    return max_profit

# Test with the given example


def test_maxProfit():
    # Test case 1: Given example
    prices1 = [7, 1, 5, 3, 6, 4]
    result1 = maxProfit(prices1)
    print(f"Input: {prices1}")
    print(f"Output: {result1}")
    print(f"Expected: 7")
    print()

    # Test case 2: Monotonically increasing
    prices2 = [1, 2, 3, 4, 5]
    result2 = maxProfit(prices2)
    print(f"Input: {prices2}")
    print(f"Output: {result2}")
    print(f"Expected: 4 (buy at 1, sell at 5)")
    print()

    # Test case 3: Monotonically decreasing
    prices3 = [7, 6, 4, 3, 1]
    result3 = maxProfit(prices3)
    print(f"Input: {prices3}")
    print(f"Output: {result3}")
    print(f"Expected: 0 (no profitable trades)")
    print()

    # Test case 4: Single day
    prices4 = [5]
    result4 = maxProfit(prices4)
    print(f"Input: {prices4}")
    print(f"Output: {result4}")
    print(f"Expected: 0 (can't trade with one day)")
    print()

    # Test case 5: Two days with profit
    prices5 = [1, 5]
    result5 = maxProfit(prices5)
    print(f"Input: {prices5}")
    print(f"Output: {result5}")
    print(f"Expected: 4")


# Run tests
test_maxProfit()
