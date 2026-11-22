class Solution:
    def romanToInt(self, s: str) -> int:
        a = 0
        i = 0 
        h = {"M":1000, "I":1, "V":5, "X":10, "L": 50, "C":100, "D": 500, "M": 1000 }

        for i in range(len(s)):
            if i+1<len(s) and h[s[i]] < h[s[i+1]]:
                a-= h[s[i]]
            else:
                a+= h[s[i]]
        return a