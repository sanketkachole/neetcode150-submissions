class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            current_reach = i + nums[i]
            if i <= farthest:
                farthest = max(current_reach, farthest)
            else:
                return False
        return True