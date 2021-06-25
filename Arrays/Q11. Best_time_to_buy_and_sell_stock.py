'''
Q11. Best time to buy and sell stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

sample i/p --> [7,1,5,3,6,4]
sample o/p --> 5

leetcode --> https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Difficult --> Easy
'''


def best_time_to_buy_sell_stock(prices):
    min_so_far = prices[0]
    max_profit = 0
    for i in prices:
        profit = i - min_so_far
        max_profit = max(profit, max_profit)
        min_so_far = min(min_so_far, i)

    return max_profit


print(best_time_to_buy_sell_stock([7, 1, 5, 3, 6, 4]))
