class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # 16/07/2026 00:44

        # create variables to store sumOdd and sumEven values
        # the sum of the first n odd numbers is always n^2
        sumOdd = n ** 2
        # the sum of the first n even numbers is always n + (n^2)
        sumEven = n * (n + 1)

        # we can immediately see that n is a common divisor
        # therefore, the GCD is n

        return n
