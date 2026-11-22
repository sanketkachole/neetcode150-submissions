class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # numSet = set(nums)
        # longest = 0

        # for n in nums:
        #     if (n-1) not in numSet:
        #         length = 0 
        #         while (n + length) in numSet:
        #             length += 1
        #         longest = max(length, longest)

        # return longest




        # 1. Convert nums into a set.
        num_set = set(nums)
        # 2. Initialize max_length = 0.
        max_length = 0
        # 3. Iterate through each number in the set:
        for n in num_set:
            # a. Check whether num - 1 exists.
            if (n - 1) not in num_set:
            # b. If num - 1 does NOT exist:
            #   - This number is the start of a sequence.
            #   - Initialize current_length = 1.
            #   - Initialize current_num = num.
                currrent_num = n
                current_length = 1
            #   - While current_num + 1 exists in the set:
            #       - Increment current_num by 1.
            #       - Increment current_length by 1.
                while (currrent_num + 1) in num_set:
                    currrent_num += 1
                    current_length += 1
            #   - Update max_length if current_length is greater.
            
                max_length = max(max_length, current_length)
        # 4. Return max_length.
        return max_length