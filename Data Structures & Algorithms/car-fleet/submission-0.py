class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_list = sorted(list(zip(position, speed)), reverse=True)
        time_to_arrival = []

        for p,s in sorted_list:
            current_time = (target - p) / s
            if len(time_to_arrival) == 0 or current_time > time_to_arrival[-1]:
                time_to_arrival.append(current_time)
            else:
                continue

        return len(time_to_arrival)
	