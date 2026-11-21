class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        rows = len(matrix)
        column = len(matrix[0])
        res = []
        for j in range(column):
            new = []
            for i  in range(rows):
                new.append(matrix[i][j])

            res.append(new)
        return res
