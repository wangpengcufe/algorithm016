��Ŀ��https://leetcode-cn.com/problems/power-of-two/   231. 2����
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0