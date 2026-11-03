class Solution:
    def minMoves(self, nums: List[int]) -> int:
        num = max(nums)
        ans = 0

        for i in nums:
            if i!= num:
                ans+= num-i

        return ans