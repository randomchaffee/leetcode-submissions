class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # 13/07/2026 01:25
        # sorting the array and create a set copy
        copy = sorted(set(arr))

        # create a dict(hashmap)
        rank = {}

        # now we populate the dict 
        # we use a dict to achieve a lower time complexity
        for i, element in enumerate(copy):
            rank[element] = i + 1

        # create an array where we can store the result
        result = []
        for num in arr:
            result.append(rank[num])
        
        # finally, we return the array with the rankings
        return result
