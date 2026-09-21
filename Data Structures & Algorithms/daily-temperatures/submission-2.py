class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indexes = []
        result = [0]* len(temperatures)

        for i in range(len(temperatures)):

            while indexes and temperatures[i] > temperatures[indexes[-1]]:
                last_index = indexes.pop()
                result[last_index] = i - last_index 
            indexes.append(i)
            
        return result