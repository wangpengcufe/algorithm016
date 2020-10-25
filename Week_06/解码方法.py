��Ŀ�� https://leetcode-cn.com/problems/decode-ways   ���뷽�� 
˼·�� # dp[i]���� s[i] ��β��ǰ׺�ַ����Ľ������
        # �������ۣ�
        # 1��s[i] != '0' ʱ��dp[i] = dp[i - 1]
        # 2��10 <= s[i - 1..i] <= 26 ʱ��dp[i] += dp[i - 2]
class Solution:
    def numDecodings(self, s: str) -> int:
        size = len(s)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]
        if s[0] == '0':
            return 0
        dp[0] = 1
        for i in range(1, size):
            if s[i] != '0':
                dp[i] = dp[i - 1]
            num = 10 * (ord(s[i - 1]) - ord('0')) + (ord(s[i]) - ord('0'))
            if 10 <= num <= 26:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
        return dp[size - 1]