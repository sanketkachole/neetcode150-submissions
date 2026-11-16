class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        path = []

        nums.sort()

        def backtrack(start, remaining):

            # 1. Successful base case
            if remaining == 0:
                results.append(path.copy())
                return

            # 2. Explore available candidates
            for i in range(start, len(nums)):

                if nums[i] > remaining:
                    break

                # 3. Make a choice
                path.append(nums[i])

                # 4. Recursive call: i allows unlimited reuse
                backtrack(i, remaining - nums[i])

                # 5. Undo the choice
                path.pop()

        # 6. Start recursion
        backtrack(0, target)

        return results