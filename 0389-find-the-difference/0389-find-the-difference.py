# Aug 06, 2026, 07:50
# I'll make a bitwise comparison approach (XOR)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        arr = []
        
        # we convert the chars into its ASCII value
        # and put each in arr
        for char in s + t:
            arr.append(ord(char))

        # we find the added char by cancelling out the values 
        # of the items in arr
        for val in arr:
            result ^= val
        
        # we convert the ASCII value back to a char
        return chr(result)
