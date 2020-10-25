��Ŀ��https://leetcode-cn.com/problems/maximal-square/ 221
˼·��ʹ��dp[i][j]��ʾ��matrix[i][j]Ϊ���½ǵĶ���Ŀ�����ɵ���������εı߳�����ô����ֻ��Ҫ�������е�i��j��ϣ�Ȼ��������ֵ����
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