class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # july 27, 2026 21:53\
        
        # we create two variables where we store the two largest
        # values in nums that we find
        largest_1 = 0
        largest_2 = 0

        # we loop through nums to find the two largest values
        for num in nums:
            if num > largest_1:
                largest_2 = largest_1
                largest_1 = num
            elif num > largest_2:
                largest_2 = num
            
        # finally, we return the maximum value minus one
        # of the two products in the array
        return ((largest_1 - 1) * (largest_2 - 1))
