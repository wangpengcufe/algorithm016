# 387. 字符串中的第一个唯一字符
#### 题目：https://leetcode-cn.com/problems/first-unique-character-in-a-string/   387. 字符串中的第一个唯一字符
#### 思路：哈希映射，O(n)
```
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = Counter(s)
        for i in range(len(s)):
            if dic.get(s[i]) == 1:
                return i 
        return -1
```

# 541. 反转字符串 II
#### 题目：https://leetcode-cn.com/problems/reverse-string-ii/  541. 反转字符串 II
#### 思路：双指针，O（n）
```
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
```

# 151. 翻转字符串里的单词
#### 题目：https://leetcode-cn.com/problems/reverse-words-in-a-string/ 151. 翻转字符串里的单词
#### 思路：split, reverse, join, O(n)
```
class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        arr.reverse()
        return ' '.join(arr)
```