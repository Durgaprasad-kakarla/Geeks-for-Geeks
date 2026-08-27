class Solution:
    def maxArea(self, mat: list[list[int]]) -> int:
        r,c=len(mat),len(mat[0])
        height = [[0] * c for _ in range(r)]

        for j in range(c):
            height[0][j] = mat[0][j]

        for i in range(1, r):
            for j in range(c):
                if mat[i][j] == 1:
                    height[i][j] = height[i - 1][j] + 1
                else:
                    height[i][j] = 0

        max_area = 0

        for i in range(r):
            sorted_row = sorted(height[i], reverse=True)  
            for j in range(c):
                max_area = max(max_area, sorted_row[j] * (j + 1))

        return max_area