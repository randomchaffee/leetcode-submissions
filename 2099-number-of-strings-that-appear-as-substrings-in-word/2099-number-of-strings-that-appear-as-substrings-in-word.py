class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # keep track of the count of valid patterns within the list
        count = 0
        # we loop through each substring in the list
        for substring in patterns:
            # for each substring in the List
            # if the substring is part of or a whole of `word`
            # we increment count, else we do nothing and move on
            # to the next value in the List
            if substring in word:
                count += 1
            else:
                continue
        
        return count