class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = 0
        for i in s+t:
            a^=ord(i)
        return chr(a)
            