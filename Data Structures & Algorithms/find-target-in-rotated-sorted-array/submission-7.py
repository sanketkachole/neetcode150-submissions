class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Initiate the left and right boundary
        left_boundary =  0 
        right_boundary = len(nums) - 1

        while left_boundary <= right_boundary: 
            mid_boundary = (left_boundary + right_boundary) // 2
            if nums[mid_boundary] == target:
                return mid_boundary


        # find the ascending sequence 
            #eg. left half sorted if Left value < Mid value 
            if nums[left_boundary] <= nums[mid_boundary]:
                if nums[left_boundary] <= target < nums[mid_boundary]:
                    right_boundary = mid_boundary - 1
                else:
                    left_boundary = mid_boundary + 1
            
            
            #eg. right half sorted right boundary > mid value
            else:
                if nums[mid_boundary] < target <= nums[right_boundary]:
                    left_boundary = mid_boundary + 1
                else:
                    right_boundary = mid_boundary - 1
                     
        return -1 

