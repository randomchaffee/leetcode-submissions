class Solution:
    def reverseDegree(self, s: str) -> int:
        total_sum = 0

        for i in range(len(s)):
            converted = (26 - (ord(s[i]) - ord('a'))) * (i + 1)
            total_sum += converted
        
        return total_sum
