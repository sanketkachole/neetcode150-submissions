class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]

        # print(freq)
        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        
        # for n, c in count.items():
        #     freq[c].append(n)
        
        # res = []
        # for i in range(len(freq) - 1, 0 , -1): 
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res



        result_dict = {}
        for num in nums:
            if num in result_dict:
                result_dict[num] += 1
            else:
                result_dict[num] = 1


        buckets = [[] for _ in range(len(nums) + 1)] # buckets 

        for num, freq in result_dict.items():
            buckets[freq].append(num)
            
        results = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                results.append(num)
                if len(results) == k:
                    return results

        return results


