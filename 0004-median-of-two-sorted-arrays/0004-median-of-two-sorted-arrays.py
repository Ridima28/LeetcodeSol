class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        a = sorted(nums1+nums2)
        n = len(a)
        if len(a) %2 == 0:

            mid1 = a[n // 2 - 1]
            mid2 = a[n // 2]

            return (mid1+mid2)/2
        
        else:

            return a[n//2]
