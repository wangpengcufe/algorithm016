class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        num3 = num5 = num7 = 0
        lis = [1]
        for i in range(k):
            temp = min(lis[num3]*3, lis[num5]*5, lis[num7]*7)
            lis.append(temp)
            if temp == lis[num3]*3:
                num3 += 1
            if temp == lis[num5]*5:
                num5 += 1
            if temp == lis[num7]*7:
                num7 += 1
        return lis[k-1]
