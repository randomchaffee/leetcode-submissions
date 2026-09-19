class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mapped = {} # create a dict

        for i, num in enumerate(nums):
            # find the complement
            complement = target - num
            # if the complement is in the array, 
            # return that and the current num's index
            if complement in mapped:
                return [mapped[complement], i]
            # else we store the current num as a key and the index as its value
            mapped[num] = i

        # if we find no answer, return an empty array
        return []