# Aug 11, 2026 08:24
# two pointer approach

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # our list of valid characters (alphanumeric)
        alnum = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        # we create two pointers, one at the start and one at the end of the string
        left = 0
        right = len(s) - 1

        while (left < right):
            if s[left] not in alnum:
                left += 1
            elif s[right] not in alnum:
                right -= 1
            else:
                # we convert them to lowercase first
                if ((s[left]).lower() != (s[right]).lower()):
                    return False
                left += 1
                right -= 1
            
        return True
        