class Solution:
    def longestPalindrome(self, s: str) -> int:
        h = {}
        res = 0
        odd = False

        for i in s:
            h[i] = h.get(i,0) +1

        for key,val in h.items():
            if val%2 == 0:
                res+= val
            else:
                odd = True
                val -=1 
                res+= val
        if odd == True:
            res+=1

        return res
