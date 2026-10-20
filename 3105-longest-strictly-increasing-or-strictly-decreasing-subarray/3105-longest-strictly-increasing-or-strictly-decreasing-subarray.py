class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing = 1
        decreasing = 1
        res = 1

        l = 0
        for r in range(1, len(nums)):
            if nums[r] == nums[r-1]:
                increasing= decreasing =1
            elif nums[r] > nums[r-1]:
                increasing += 1
                decreasing = 1

            elif nums[r-1]> nums[r]:
                decreasing +=1
                increasing =1

            res = max(res, increasing, decreasing)

        return res