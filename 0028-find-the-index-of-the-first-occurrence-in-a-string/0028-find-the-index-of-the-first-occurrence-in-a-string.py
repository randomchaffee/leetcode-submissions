# a not so efficient solution

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        # we iterate through the max length of the subset
        for i in range(len(haystack) - len(needle) + 1):
            match = True
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    match = False
                    break
                
            if match:
                return i

        
        # if the loop finishes, we return 1 (fail)
        return -1
