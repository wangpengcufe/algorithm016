# ̰�ķ���ֱ�ӱȽϵ�ǰԪ�غ�ǰһ��Ԫ��
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)):
            if i >0 and prices[i-1] < prices[i]:
                result += (prices[i] - prices[i-1])
        return result