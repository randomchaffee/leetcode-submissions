class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # get the size of the array
        sizeOfArray = len(nums)

        # since we already assume that the majority element
        # always exists in the array, we can spare adding
        # edge case checks

        # create a map to keep track of counts
        counts = {}

        for num in nums:
            # if currently not in the dict, add it
            if num not in counts:
                counts[num] = 1
            # check if it reached the majority threshold
            # if it has, return the value
            if counts[num] > sizeOfArray / 2:
                return num
            # if it hasnt yet, just increment it
            counts[num] += 1
        
        return None