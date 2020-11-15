题目：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/   557. 反转字符串中的单词 III
思路：split, 单词翻转，join， 字符串翻转， O（n）
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split(" ")[::-1])[::-1]