class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # Initialize
        # max_profit = 0
        # lowest_value = prices[0]

        # # Iterate through each element
        # for i in prices:
        #     # check the lowest value so far
        #     if i < lowest_value:   
        #         lowest_value = i 
        #     profit = i - lowest_value 

        #     if profit > max_profit:
        #         max_profit = profit

        # return max_profit





        buying_index = 0
        selling_index = 1
        max_profit = 0 

        while selling_index < len(prices):
            profit = prices[selling_index] - prices[buying_index]

            if prices[selling_index] < prices[buying_index]:
                buying_index = selling_index
                
            selling_index += 1
            
            max_profit = max(max_profit, profit)

        return max_profit


