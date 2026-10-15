class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Initialization
        left_boundary_speed = 1
        right_boundary_speed = max(piles)
        best_speed = max(piles)

        # Binary search
        while left_boundary_speed <= right_boundary_speed:
            mid_boundary_speed = (left_boundary_speed + right_boundary_speed) // 2

            total_hours = 0

            # Calculate the hours
            for i in piles:
                hours = (i + mid_boundary_speed - 1) // mid_boundary_speed
                total_hours += hours

            # Decision
            if total_hours <= h:
                best_speed = mid_boundary_speed
                right_boundary_speed = mid_boundary_speed - 1
            else:
                left_boundary_speed = mid_boundary_speed + 1

        # Termination
        return best_speed
