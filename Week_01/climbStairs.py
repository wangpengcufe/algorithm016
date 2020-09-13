"""
假设你正在爬楼梯。需要 n?阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

链接：https://leetcode-cn.com/problems/climbing-stairs
"""
class Solution(object):
    def climbStairs(self, n):
        f0 = 0
        f1 = 1
        f2 = 2
        if n<=0:
            return f0
        elif n==1:
            return f1
        elif n==2:
            return f2
        else:
            result = 0
            for i in range(3,n+1):
                result = f1+f2
                f1 = f2
                f2 = result
        return result