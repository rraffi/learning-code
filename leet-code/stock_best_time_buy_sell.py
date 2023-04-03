# Use two-pointer or sliding window technique
# left pointer tracks buying price of stock
# right pointer tracks selling price of stock
# profit = right pointer price minus left pointer price.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                maxP = max(maxP, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxP


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,6,4,3,1]))