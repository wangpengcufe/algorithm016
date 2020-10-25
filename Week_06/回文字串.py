��Ŀ��https://leetcode-cn.com/problems/palindromic-substrings/   647
˼·����̬�滮dp,�ַ���s[i?j]�Ƿ�Ϊ�����Ӵ�������ǣ�dp[i][j]=true��
�������, dp[i][j]=false������base case�������Զ��׼�����ֻ��һ����ĸ��ʱ��϶��ǻ����Ӵ���
Ϊʲô�����½Ǳ�������Ϊ����dp��ʱ��(i, j) λ�õ�ֵ�����ڣ�i+1,j-1����
Ҳ���ǵ�ǰλ�õ����·�����Ȼ����������±��������·���ֵ����ȫû�г�ʼ����
��Ȼ��ǰλ��Ҳ���Ǵ���ġ����Ǵ����½Ǳ����ͱ�֤�����·�������ֵ���Ѿ�������ˡ�

class Solution:
    def countSubstrings(self, s: str) -> int:
        if s is None or s == "":
            return 0
        n = len(s)

        dp = [[False for i in range(n)] for j in range(n)]
        result = len(s)

        for i in range(n):
            # base case: ֻ��һ����ĸ��ʱ��϶��ǻ����Ӵ�
            dp[i][i] = True
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i == 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    result += 1
        return result