class Solution:
    def trap(self, height: List[int]) -> int:
        left_max_height = [height[0]]
        right_max_height = [height[len(height)-1]]
        trapped_water = 0
        for i in range(1, len(height)):
            left_max_height.append(max(left_max_height[i-1], height[i]))

        for i in range(len(height)-2, -1, -1):
            right_max_height.append(max(right_max_height[-1], height[i]))

        right_max_height.reverse()

        for i in range(len(height)):
            trapped_water += (min(left_max_height[i], right_max_height[i]) - height[i])
            
        return trapped_water        