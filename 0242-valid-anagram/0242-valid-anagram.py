class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # july 25 2026, 17:42
        
        # we can immediately conclude that the case is not
        # an anagram if their lengths differ
        if len(s) != len(t):
            return False
        
        # first, we create a dict (hash map) that we will use to 
        # keep track of the number of occurences for each char in s
        frequency_map = {}

        # we loop through s, adding/incrementing the count of occurences
        # for each char in the string
        for char in s:
            frequency_map[char] = frequency_map.get(char, 0) + 1
        
        # we do the same for t, but in reverse. instead of incrementing,
        # we decrement the count value
        for char in t:
            frequency_map[char] = frequency_map.get(char, 0) - 1

        # if all values in the hash_map are equal to 0,
        # it should mean that s contains the exact same characters as t
        # (an anagram)
        is_zero = all(v == 0 for v in frequency_map.values())

        # finally, we return the boolean value of is_zero
        return is_zero