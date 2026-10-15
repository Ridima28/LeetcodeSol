class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        area = 0
        stack = []

        for i, height in enumerate(heights):
            start = i 
            while stack and height < stack[-1][0]:
                h,j = stack.pop()
                w = i-j
                a = h*w
                area = max(area, a)
                start = j
            stack.append((height, start))


        while stack:
            h,j = stack.pop()
            w = n-j
            a = h*w
            area = max(area,  a)

        return area
