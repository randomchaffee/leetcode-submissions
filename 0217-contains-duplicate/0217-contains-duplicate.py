class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # create a set to track seen values
        seen = set()

        # iterate thru the array
        # return true immediately if we encounter a num
        # already in seen (the set)
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        # if we find nothing, return false
        return False