class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # pos, pos -> extend
        # pos, neg -> new
        # neg, pos -> extend
        # neg, neg -> new
        currentSum = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):
            currentSum = max(nums[i], currentSum + nums[i])
            maxSum = max(maxSum, currentSum)
        
        return maxSum
