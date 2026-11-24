class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        h = {}


        for i in strs:
            sorte = "".join(sorted(i))
            if sorte not in h:
                h[sorte] = [i]
            else:
                h[sorte].append(i)

        return list(h.values())
        #h = {"eat": [eat, tea, ate], "tan": [tan, nat], "bat": [bat]}