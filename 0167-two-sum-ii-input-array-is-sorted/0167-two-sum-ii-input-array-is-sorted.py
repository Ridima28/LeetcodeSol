class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        ans = [] 
        # h = {}
        # for i in range(len(numbers)):
        #     compli = target-numbers[i]
        #     if compli in h:
        #         ans.append([h[i]+1, i])

        l = 0
        r = len(numbers)-1
        cur = 0
        while l<r:
            cur =  numbers[l] + numbers[r]
            if cur == target:
                return [l+1, r+1]
            elif cur > target:
                r-=1 
            else:
                l+=1
