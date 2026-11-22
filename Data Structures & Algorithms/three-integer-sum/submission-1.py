class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # empty_list = []
        # nums.sort()
        # for i in range(len(nums) - 2):
        
        #     if i > 0 and nums[i] == nums[i -1]:
        #         continue

        #     fixed_number = nums[i]    
        #     left = i + 1
        #     right = len(nums) - 1

        #     while left < right:
        #         if fixed_number + nums[left] + nums[right] < 0:
        #             left += 1
        #         elif fixed_number + nums[left] + nums[right] > 0:
        #             right -= 1
        #         else:
        #             empty_list.append([fixed_number, nums[left], nums[right]])
        #             left += 1
        #             right -= 1
        #             while left < right and nums[left] == nums[left-1]:
        #                 left += 1
        #             while left < right and nums[right] == nums[right+1]:
        #                 right -= 1
        # return empty_list

        nums.sort()
        results = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if -nums[i] < nums[j] + nums[k]:
                    k -= 1
                elif -nums[i] > nums[j] + nums[k]:
                    j += 1
                else:
                    results.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return results	