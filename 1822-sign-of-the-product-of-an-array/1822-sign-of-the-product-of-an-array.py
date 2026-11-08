class Solution:
    def arraySign(self, nums: list[int]) -> int:
        pro = 1
        for i in nums:
            pro *= i

        h = {"neg": 0}
        for j in nums:
            if j<0:
                h["neg"] +=1
        if pro == 0:
            return 0
        elif pro <0:
            return -1
        else:
            return 1


            