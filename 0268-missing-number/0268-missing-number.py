# Aug 04, 2026 20:10

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # since the numbers are distinct and range from 0 to n
        # we can assume that the sum of all values in the list
        # is [n * (n + 1)]/2 (the arithmetic series)

        # if we take the sum of the arithmetic series with the length of nums
        total = 0
        for i in range(len(nums) + 1):
            total += i

        # we can use that answer and subtract it with the sum of all elements in nums
        sum_of_nums = 0
        for num in nums:
            sum_of_nums += num
        
        # the difference should be the missing number
        return total - sum_of_nums
