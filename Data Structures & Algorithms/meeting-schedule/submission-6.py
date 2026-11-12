"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda x :x.start)

        non_overlapping_intervals = [] 

        for interval in intervals:
            start = interval.start
            end = interval.end
            
            if non_overlapping_intervals and start < non_overlapping_intervals[-1].end:
                return False
            else:
                non_overlapping_intervals.append(interval)
            
        return True

		