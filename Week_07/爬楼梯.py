题目：https://leetcode-cn.com/submissions/detail/117150368/  70.爬楼梯 
思路：动态方程dp，dp存的是结果，和num产生联系，即动态方程
# 遇到想要跳过 if n==0：continue的情况，可以直接把遍历范围从1开始遍历，1到n
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(1, n):
            dp[i+1] = dp[i-1] + dp[i]
        return dp[-1]