class Solution:
    """
    @param: str: list of strings
    @return: encode a list of strings to a single string. 
    """
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    """
    @param: str: A string
    @return: decode a single string to a list of strings
    """        
    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return res



