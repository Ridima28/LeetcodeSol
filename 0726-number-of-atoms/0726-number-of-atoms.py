class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i = 0
        while i<len(formula):
            if formula[i] == "(":
                stack.append(defaultdict(int))
            elif formula[i] == ")":
                curr_map = stack.pop()
                count = ""
                while i+1<len(formula) and formula[i+1].isdigit():
                    count+= formula[i+1]
                    i+=1
                count = 1 if not count else int(count)
                prev_map = stack[-1]
                for elem in curr_map:
                    prev_map[elem] += curr_map[elem]*count
            else:
                # for cases like Mg
                element = formula[i]
                count = ""
                while i+1<len(formula) and formula[i+1].islower():
                    element += formula[i+1]
                    i+=1
                while i+1<len(formula) and formula[i+1].isdigit():
                    count += formula[i+1]
                    i+=1
                count = 1 if not count else int(count)
                curr_map = stack[-1]
                curr_map[element] += count

            i+=1

        cnt_map = stack[-1]

        res = ""
        for eleme in sorted(cnt_map.keys()):
            count ="" if cnt_map[eleme] == 1 else cnt_map[eleme]
            res += eleme+str(count)

        return res 
