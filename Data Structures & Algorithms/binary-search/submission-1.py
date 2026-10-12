class Solution:
	def	search(self, array: List[int], target: int) -> int:


		# Use binary search. First is leftmost index = 0 and right is lenth(array) - 1 
		left_index = 0
		right_index = len(array)-1

		while left_index <= right_index:
			# find the middle element number 
			mid_index = (left_index + right_index ) // 2
				
			#  if the target is equal to mid_index_value return mid_index	
			if array[mid_index] == target:
				return mid_index
			#  if the target is largrt then mid_index_value 
				# update the left_index = mid_index + 1
			elif array[mid_index] < target:
				left_index = mid_index + 1
			#  if the target is smaller then mid_index_value    
				# update the right_index = mid_index - 1 
			elif array[mid_index] > target:
				right_index = mid_index - 1
			
		else:
			return -1