class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        h = {}
        half = len(nums) /3

        for i in nums:
            h[i] = h.get(i, 0) +1
        ans = []
        for key, val in h.items():
            if val > half:
                ans.append(key)
        return ans