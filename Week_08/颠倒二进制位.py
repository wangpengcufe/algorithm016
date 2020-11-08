题目：https://leetcode-cn.com/problems/reverse-bits/   190. 颠倒二进制位
class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret