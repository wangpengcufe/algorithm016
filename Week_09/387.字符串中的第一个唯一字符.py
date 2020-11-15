题目：https://leetcode-cn.com/problems/first-unique-character-in-a-string/   387. 字符串中的第一个唯一字符
思路：哈希映射
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = Counter(s)
        for i in range(len(s)):
            if dic.get(s[i]) == 1:
                return i 
        return -1
