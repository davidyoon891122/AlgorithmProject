
from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        print(profit)
        print(min_price)


nums = [7, 1, 5, 3, 6, 4]

s = Solution()
s.maxProfit(prices=nums)