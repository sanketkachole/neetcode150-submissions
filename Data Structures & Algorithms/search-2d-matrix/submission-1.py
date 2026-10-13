class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		left_index = 0
		rows = len(matrix)
		cols = len(matrix[0])
		total_elements = rows * cols
		right_index = total_elements - 1


		while right_index >= left_index:
			mid_index = (left_index + right_index) // 2
			new_rows = mid_index // cols
			new_cols = mid_index % cols
			
			if  target == matrix[new_rows][new_cols]:
				return True
			elif target > matrix[new_rows][new_cols]:
				left_index = mid_index + 1
			elif target < matrix[new_rows][new_cols]:
				right_index = mid_index - 1
		return False
