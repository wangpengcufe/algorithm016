��Ŀ��https://leetcode-cn.com/submissions/detail/117150368/  70.��¥�� 
˼·����̬����dp��dp����ǽ������num������ϵ������̬����
# ������Ҫ���� if n==0��continue�����������ֱ�Ӱѱ�����Χ��1��ʼ������1��n
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(1, n):
            dp[i+1] = dp[i-1] + dp[i]
        return dp[-1]