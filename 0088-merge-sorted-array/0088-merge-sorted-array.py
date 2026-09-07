class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        cnt = n + m - 1

        while n > 0:
            # edge case: to avoid index out of bounds error
            if m == 0:
                if n == 0:
                    nums1[cnt] = nums1[m - 1]
                    m -= 1
                    cnt -= 1
                    continue
                nums1[cnt] = nums2[n - 1]
                n -= 1
                cnt -= 1
                continue
            if nums1[m - 1] > nums2[n - 1]:
                nums1[cnt] = nums1[m - 1]
                m -= 1
                cnt -= 1
            else:
                nums1[cnt] = nums2[n - 1]
                n -= 1
                cnt -= 1