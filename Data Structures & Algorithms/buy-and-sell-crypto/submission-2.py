class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize
        max_profit = 0
        lowest_value = prices[0]

        # Iterate through each element
        for i in prices:
            # check the lowest value so far
            if i < lowest_value:   
                lowest_value = i 
            profit = i - lowest_value 

            if profit > max_profit:
                max_profit = profit

        return max_profit



