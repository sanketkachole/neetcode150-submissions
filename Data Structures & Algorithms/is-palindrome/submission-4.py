class Solution:
    def isPalindrome(self, s: str) -> bool:
    #     l, r = 0, len(s) - 1

    #     while l < r:            
    #         while l < r and not self.alphaNum(s[l]):
    #             l += 1
    #         while r > l and not self.alphaNum(s[r]):
    #             r -= 1
    #         if s[l].lower() != s[r].lower():
    #             return False
    #         l, r = l + 1, r - 1
    #     return True




    # def alphaNum(self, c):
    #     return (
    #             ord('A') <= ord(c) <= ord('Z') or
    #             ord('a') <= ord(c) <= ord('z') or
    #             ord('0') <= ord(c) <= ord('9')
    #             )



        i = 0 
        j = len(s) - 1


        while i < j:
            while not s[i].isalnum() and i<j :
                i += 1
            while not s[j].isalnum() and i<j :
                j -= 1
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True














