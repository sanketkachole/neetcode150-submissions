class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        # prevMap = {}

        # for i, n in enumerate(nums):
        #     #print(i)
        #     #print(n)

        #     diff = target - n
        #     if diff in prevMap:
        #         return [prevMap[diff], i]
        #     prevMap[n] = i
                       


        empty_hash_map = {}

        for i in range(len(nums)):
            second_number = target - nums[i]
            if second_number in empty_hash_map:
                return [empty_hash_map[second_number], i]
            else:
                empty_hash_map[nums[i]] = i
