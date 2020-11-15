题目：https://leetcode-cn.com/problems/reverse-words-in-a-string/ 151. 翻转字符串里的单词
思路：split, reverse, join, O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        arr.reverse()
        return ' '.join(arr)