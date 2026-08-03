# Aug 03, 2026 20:44

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we create a pointer for our buy day
        left = 0
        # where we set our profit
        max_profit = 0

        for right in range(1, len(prices)):
            # if the current price is lower than our buy price
            # we move left to right
            if prices[right] < prices[left]:
                left = right
            else:
                # we calculate the profit and update if it's higher
                curr_profit = prices[right] - prices[left]
                max_profit = max(max_profit, curr_profit)
        
        return max_profit
