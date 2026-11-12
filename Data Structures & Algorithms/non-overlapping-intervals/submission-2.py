class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[1])

        merged = []
        removed_intervals = []
        for start, end in intervals:
            # if second list is overlapping with first 
            # end is < than merged[-1][1]
            if merged and start < merged[-1][1]: 
                removed_intervals.append([start, end])
            
            # if second list is non overlapping
            # end is >= merged[-1][1]
            else:
                merged.append([start, end])
                
        return len(removed_intervals)

		
		