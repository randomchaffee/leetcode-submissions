# Aug 06, 2026, 07:44
# I'll make a string value approach (typecasting)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_value = 0
        t_value = 0
        # get the sum of the ASCII values of s
        for char in s:
            s_value += ord(char)
        
        # get the sum of the ASCII values of t
        for char in t:
            t_value += ord(char)
        
        # the difference of the two should return the value of 
        # the added_letter
        # now we just need to typecast it back into a char
        return chr(t_value - s_value)
