class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        word = collections.defaultdict(set)
        for i in ideas:
            word[i[0]].add(i[1:])

        res = 0
        for char1 in word:
            for char2 in word:
                if char1 == char2:
                    continue
                intersect = 0

                intersect = len(word[char1] & word[char2])


                distinct1 = len(word[char1])- intersect
                distinct2 = len(word[char2])- intersect
                res+= distinct1 * distinct2
        return res