class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #Initialization of both boundaries.
        left_index = 0
        right_index = len(nums) - 1

        # Loop termination whenthe boundaries meet. 
        while left_index != right_index:

            # Find mid_index = (left_index + right_index)//2
            mid_index = (left_index + right_index)//2
            
            # compare the mid_index with the right
            #if mid_value is larger than right_value then min is at right.
            #assign left_index = mid_index + 1 and follow the procedure
            if nums[mid_index] > nums[right_index]:
                left_index = mid_index + 1
            
            #if the mid_value < right_value then eliminate the right side. 
            #move the binary search towards the left. right_index = mid_index
            else:
                right_index = mid_index
                
        return nums[right_index]
