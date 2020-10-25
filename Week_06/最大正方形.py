题目：https://leetcode-cn.com/problems/maximal-square/ 221
思路：使用dp[i][j]表示以matrix[i][j]为右下角的顶点的可以组成的最大正方形的边长。那么我们只需要计算所有的i，j组合，然后求出最大值即可
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res = 0
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 if matrix[i - 1][j - 1] == "1" else 0
                res = max(res, dp[i][j])
        return res ** 2