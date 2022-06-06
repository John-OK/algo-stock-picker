# 1. Iterate through each number in array and iterate through other nums to find largest difference for that number.
# 2. Check if diff between nums (higher index num - lower index num) is greater than current max, if so, store indices of the pair: [lower index, higher index]
# 3. Return array of pair of indices


def picker(prices):
    max_profit = 0
    max_profit_pair = []

    for i in range(len(prices) - 1):
        buy = prices[i]
        for j in range(i + 1, len(prices)):
            sell = prices[j]
            profit = sell - buy
            if profit > max_profit:
                max_profit = profit
                max_profit_pair = [i, j]
    return max_profit_pair

# days = picker([1,2])
# print(days)