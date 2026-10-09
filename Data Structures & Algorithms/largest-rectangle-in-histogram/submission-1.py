class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # intialize an empty stack
        height_stack = []
        # initialize maximum area with zero
        max_area = 0
        # loop through each bar with its index and height
        for index, height in enumerate(heights):
            # set the current bar's tentative start index to its own index
            start_index = index
            # while the stack is not empty and the current height is smaller than the top stack height, pop the top entry
            while height_stack and height < height_stack[-1][-1]:
                # remove the top stack entry and get its stored start index and height
                popped_start, popped_height = height_stack.pop()
                # calculate the popped rectangle's width using current index - popped start index
                width = index - popped_start
                # calculate its area using popped height * width
                area = popped_height * width
                # update maximum area if the popped rectangle's area is larger
                max_area = max(max_area, area)
                # update the current bar's tentative start index to the popped start index
                start_index = popped_start
            # if the current height is equal to the top stack height then keep the top stack as it is with its index
            if height_stack and height == height_stack[-1][1]:
                continue
                
            height_stack.append((start_index, height))
            
        n = len(heights)

        # for each remaining entry in the stack
        for start_index, height in height_stack:
            # calculate width using array length - stored start index
            width = n - start_index
            # calculate area using stored height * width
            area = height * width
            # update maximum area if this area is larger
            max_area = max(max_area, area)

        # return maximum area
        return max_area