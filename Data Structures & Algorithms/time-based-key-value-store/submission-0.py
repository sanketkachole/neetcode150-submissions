class TimeMap:
	
	def __init__(self):
		# Create empty dictionary
		self.timemap = {}

	def set(self, key:str, value: str, timestamp: int) -> None:
		# check if the key not exist in empty dictionary
		if key not in self.timemap:
			self.timemap[key] = []
		self.timemap[key].append([value, timestamp])
	

	def get(self, key: str, timestamp: int) -> str:
		if key not in self.timemap:
			return ""
		else:
			left_boundary = 0
			right_boundary = len(self.timemap[key]) - 1
			mood_so_far = ""
			while left_boundary <= right_boundary:
				mid_boundary = (left_boundary + right_boundary) //2
				if self.timemap[key][mid_boundary][1] == timestamp:
					return self.timemap[key][mid_boundary][0]
				elif self.timemap[key][mid_boundary][1] <= timestamp:
					mood_so_far = self.timemap[key][mid_boundary][0]
					left_boundary = mid_boundary + 1
				else:
					right_boundary = mid_boundary - 1
					
		return 	mood_so_far
        
