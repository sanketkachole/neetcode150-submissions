"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted(interval.start for interval in intervals)
        end = sorted(interval.end for interval in intervals)

        s = 0
        e = 0
        counter = 0 
        max_rooms = 0
        while s < len(start):
            if start[s] < end[e]:
                counter += 1
                s += 1
                max_rooms = max(max_rooms, counter)
            elif start[s] > end[e]:
                counter -= 1
                e += 1
            else:
                s += 1
                e += 1
        return max_rooms





