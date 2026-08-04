# Aug 04, 2026
# NOTE: a better approach I think. this one exits immediately (True) if a duplicate is found

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a set where we record found values
        seen = set()

        # we iterate through the array, checking whether each value
        # is already in the set (seen)
        for num in nums:
            if num in seen:
                # if it already is, we can exit early and return True
                return True
            # if not, we add the value to the set
            seen.add(num)
        
        return False
            