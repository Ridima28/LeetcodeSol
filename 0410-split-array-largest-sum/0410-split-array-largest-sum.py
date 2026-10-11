class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:

        start = max(nums)
        end = sum(nums)

        while start < end:
            mid = (start+end)//2

            total = 0 
            count = 1 
            for i in nums:
                total += i
                if total>mid:
                    count +=1
                    total = i

            if count>k:
                start = mid+1

            else:
                end = mid
        return end