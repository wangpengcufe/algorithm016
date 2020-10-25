# 题目：https://leetcode-cn.com/problems/minimum-path-sum
# 思路：动态规划，dp存储的是结果，和num产生联系，即动态方程，O（n^2）
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        dp = grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i][j] += dp[i][j-1]
                elif j == 0:
                    dp[i][j] += dp[i-1][j]
                else:
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]