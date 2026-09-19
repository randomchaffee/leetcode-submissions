class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        # edge case if length of s is less than 10
        if len(s) <= 10:
            return []

        # create a hashmap to add and count frequency of length 10 substrings
        substrings = {}
        for l in range(len(s) + 1):
            r = l + 10 # add 1 more due to slicing rules
            # exit if r is at the end
            if r > len(s):
                break

            # slice the substring and check if it is in the hashmap
            sub = s[l:r]
            if sub not in substrings:
                substrings[sub] = 1
            else:
                substrings[sub] += 1 # increment its value if already present
        
        # gather all keys in the hashmap and return only those with
        # counts greater than 1
        for key in list(substrings.keys()):
            if substrings[key] < 2:
                del substrings[key]
        
        return list(substrings.keys())
