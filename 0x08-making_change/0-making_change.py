#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    return fewest number of coins needed to meet the total
        if total is 0 or less return 0
        if total cannot be met by any number of coins return -1
    """

    if not isinstance(coins, list):
        print("coins must be a list of coin denominations")
        return

    if total <= 0:
        return 0

    # sort the coins in descending order
    coin_count = 0
    coin_len = len(coins)
    coins.sort(reverse=True)

    for i in range(coin_len):
        # check if total is greater than the first coin, if not move to next
        while total and total >= coins[i]:
            total = total - coins[i]
            coin_count += 1

    if total == 0:
        return coin_count
    else:
        return -1
