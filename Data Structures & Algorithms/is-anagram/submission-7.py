class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # count = [0] * 26
        # count
        # if len(s) != len(t):
        #     return False

        # for i in range(len(s)):
        #     count[ord(s[i]) - ord('a')] += 1
        #     count[ord(t[i]) - ord('a')] -= 1

        # for val in count:
        #     if val != 0:
        #         return False
        # return True


		
        frequency_s = {}
        frequency_t = {}

        for char in s:
            frequency_s[char] = frequency_s.get(char, 0) + 1
        for char in t:
            frequency_t[char] = frequency_t.get(char, 0) + 1
            
        if frequency_s == frequency_t:
            return True
        else:
            return False


