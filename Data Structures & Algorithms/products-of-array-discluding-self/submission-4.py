class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = [1] * (len(nums))

        # prefix = 1
        # for i in range(len(nums)): 
        #     res[i] = prefix
        #     prefix *= nums[i]
        # postfix = 1
        # for i in range(len(nums)-1, -1, -1):
        #     res[i] *= postfix
        #     postfix *= nums[i]
        # return res
        


        left = [1] * len(nums)
        right = [1] * len(nums)
        results = []
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i - 1]

        for i in range(len(nums)-2, -1, -1): # 2, 1, 0   
            right[i] = nums[i + 1] * right[i + 1]
            
        for i in range(len(nums)):
            results.append(left[i] * right[i])

        return results
