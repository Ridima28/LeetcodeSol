class Solution:
    def decodeString(self, s: str) -> str:

        stack =[]

        for i in range(len(s)):
           

            if s[i] != "]":
                stack.append(s[i])
            else:
                alpha = ""
                while stack[-1] != "[":
                    alpha = stack.pop()+alpha

                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() +k

                stack.append(int(k) * alpha)

        return "".join(stack)