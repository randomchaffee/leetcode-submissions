# Aug 06, 2026, 07:19
# I'll make a hashmap approach

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # we create a hashmap (dict) to map out the values in s
        initial = {}
        for char in s:
            # reminder for self: get(key, default_value) NOT THE CURRENT VALUE
            initial[char] = initial.get(char, 0) + 1
        
        # then we iterate through t, and subtract 1 in the value of the keys
        # in initial
        for char in t:
            # if we encounter the added letter in t and it is not in the map, 
            # we mark it as -1
            initial[char] = initial.get(char, -1) - 1
        
        added_letter = ""
        for key in initial:
            # if a key is NOT 0, we found the added_letter
            if initial[key] != 0:
                added_letter += key
                
        return added_letter

        
