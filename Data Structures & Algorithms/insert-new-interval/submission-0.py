class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # Step 1: Initialize an empty result list.
        results = []

        # Step 2: Loop through each existing interval.
        for interval in intervals:
            # Case 1: Existing interval comes BEFORE the new interval.
            # If current interval's end < new interval's start:
                # Append the current interval to the result.
            if interval[1] < newInterval[0]:
                results.append(interval)
            
            # Case 2: Existing interval comes AFTER the new interval.
            # Else if current interval's start > new interval's end:
                # Append the new interval to the result.
                # Replace the new interval with the current interval.
                # This ensures the new interval is not inserted twice.
            elif interval[0] > newInterval[1]:
                results.append(newInterval)
                newInterval = interval
            # Case 3: Existing interval OVERLAPS the new interval.
            # Else:
                # Update new interval's start using the minimum of both starts.
                # Update new interval's end using the maximum of both ends.
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        # Step 3: Append the remaining new interval to the result.

        results.append(newInterval)
        # Step 4: Return the result.
        return results
