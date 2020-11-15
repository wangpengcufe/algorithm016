题目：https://leetcode-cn.com/problems/reverse-string-ii/  541. 反转字符串 II
思路：双指针，O（n）
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2*k):
            left = i 
            right = i + k -1 if i + k - 1 < len(s) else len(s) - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)