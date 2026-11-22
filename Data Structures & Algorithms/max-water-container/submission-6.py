class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # left = 0
        # right = len(heights) - 1
        # max_area = 0

        # while left < right:
        #     area = min(heights[left],heights[right]) * (right - left)
        #     if area > max_area:
        #         max_area = area

        #     if heights[left] < heights[right]:
        #         left += 1
        #     else:
        #         right -= 1    
        # return max_area		
        
        i = 0
        j = len(heights) - 1
        max_area = 0

        while i < j:	
            current_area = min(heights[i], heights[j]) * (j - i)
            max_area = max(max_area, current_area)	
            
            if heights[i] < heights[j]:
                i += 1	
            else:
                j -= 1

        return max_area



