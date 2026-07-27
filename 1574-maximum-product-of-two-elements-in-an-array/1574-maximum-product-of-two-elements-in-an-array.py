class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # july 27, 2026 21:53
        
        # first we create a variable to store the maximum we find
        # as the nested loop progresses
        maximum = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                # we skip if i and j are of the same index value
                if i == j:
                    continue

                # we do the operation
                curr = (nums[i] - 1) * (nums[j] - 1)
                
                # we check if the current calculation results in
                # a larger product than the current maximum
                if curr > maximum:
                    maximum = curr
        
        return maximum
