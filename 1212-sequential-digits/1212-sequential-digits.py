class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # 13/07/2026 21:36
        # create an array of integers
        nums = [12, 23, 34 , 45, 56, 67, 78, 89,
                123, 234, 345, 456, 567, 678, 789,
                1234, 2345, 3456, 4567, 5678, 6789,
                12345, 23456, 34567, 45678, 56789,
                123456, 234567, 345678, 456789,
                1234567, 2345678, 3456789,
                12345678, 23456789,
                123456789]

        # create an array where we will store the valid digits
        sequential_digits = []
        
        # we loop through `nums` and append digits that are within
        # the range of `low` and `high`
        for num in nums:
            # note: we need to add +1 to high since range is exclusive 
            # of the high value
            if num in range(low, high + 1):
                sequential_digits.append(num)

        # finally, we return `sequential_digits`
        return sequential_digits