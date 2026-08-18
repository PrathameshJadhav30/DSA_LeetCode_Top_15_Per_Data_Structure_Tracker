def max_profit(prices):
    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):

        # Minimum price seen so far
        min_price = min(min_price, prices[i])

        # Profit if we sell today
        profit = prices[i] - min_price

        # Maximum profit so far
        max_profit = max(max_profit, profit)

    return max_profit


# Input
n = int(input("Enter number of days: "))

prices = list(map(int, input("Enter stock prices: ").split()))

# Calculate result
result = max_profit(prices)

print("Maximum Profit =", result)