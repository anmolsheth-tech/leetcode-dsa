#right is used for scanning in this case, hence the while condition is structured like that
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            right += 1
        return maxProfit
