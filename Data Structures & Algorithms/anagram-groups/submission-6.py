class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list)
        # for word in strs:
        #     count = [0] * 26    
            
        #     for s in word:
        #         count[ord(s) - ord('a')] += 1
            
        #     res[tuple(count)].append(word)

        # return list(res.values())
        result_dict = {}
        for word in strs:
            freq_vect = 26 * [0]
            for letter in word:
                freq_vect[ord(letter) - ord('a')] += 1
            
            if tuple(freq_vect) in result_dict:
                result_dict[tuple(freq_vect)].append(word)
            else:
                result_dict[tuple(freq_vect)] = [word]
        return list(result_dict.values())




