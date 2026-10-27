class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #seen = set()
        #for num in nums:
        #    if num in seen:
        #        return True
        #    seen.add(num)
        #return False

        storage_set = set()
        for i in nums: 
            if i in storage_set: 
                return True
            else: 
                storage_set.add(i)
        return False
                    
