class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:

            # Decide whether to extend the existing subarray
            # or start a new subarray from the current number.
            current_sum = max(num, current_sum + num)

            # Track the maximum sum found so far.
            max_sum = max(max_sum, current_sum)

        return max_sum