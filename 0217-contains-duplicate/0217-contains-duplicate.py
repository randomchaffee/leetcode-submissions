# Aug 04, 2026
# NOTE: this solution is suboptimal. I don't think creating a hash map is needed 
#       and just makes the process slower. But this is just how my solution would
#       be if I didn't think of the time and space complexity

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a hash map where we will count the occurences of each num
        occurences = {key: 0 for key in nums}

        # we iterate through the array, incrementing the occurences
        # for each item encountered
        for num in nums:
            if num in occurences:
                occurences[num] += 1

        # if there are any values with more than 1 occurence,
        # we return True, otherwise return False        
        for key, value in occurences.items():
            if value > 1:
                return True

        return False